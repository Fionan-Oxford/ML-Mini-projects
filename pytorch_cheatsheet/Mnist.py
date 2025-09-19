# type: ignore
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

train_ds = datasets.MNIST(root="data", train=True, transform=ToTensor(), download=True)
test_ds = datasets.MNIST(root="data", train=False, transform=ToTensor(), download=True)

BATCH_SIZE = 16

train_dl = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)
test_dl = DataLoader(test_ds, batch_size=BATCH_SIZE, shuffle=False)

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"using {device}")


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


model = NeuralNetwork().to(device)
print(model)


def train(dataloader, model, loss_fn, optimiser):

    size = len(dataloader.dataset)
    model.train()

    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)  # Move data to the same device as the model

        # Compute the prediction error

        pred = model(X)
        loss = loss_fn(pred, y)

        # backpropogation
        loss.backward()
        optimiser.step()
        optimiser.zero_grad()

        if batch % 100 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def eval(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size

    print(f"Test Error: \n Accuracy: {(100*correct)}, Avg Loss {test_loss} \n")


epochs = 20
loss_fn = nn.CrossEntropyLoss()
optimiser = torch.optim.AdamW(model.parameters(), lr=1e-3)

for t in range(epochs):
    print(f"Epocj {t + 1}")
    train(train_dl, model, loss_fn, optimiser)
    eval(test_dl, model, loss_fn)
print("Done!")
