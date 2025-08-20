# type: ignore

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from torch.utils.data.distributed import DistributedSampler


# ---------- Model ----------
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 50)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(50, 2)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)  # raw logits (CrossEntropyLoss expects logits)
        return x


# ---------- Training (synchronous DP with DistributedSampler) ----------
def train_sync_dp_with_distributedsampler(
    num_epochs: int = 3,
    world_size: int = 2,  # number of simulated workers
    batch_size: int = 16,
    lr: float = 0.05,
    seed: int = 42,
):
    torch.manual_seed(seed)

    # Synthetic dataset
    data = torch.randn(100, 10)
    labels = torch.randint(0, 2, (100,))
    dataset = TensorDataset(data, labels)

    model = SimpleModel()
    optimizer = optim.SGD(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()

    # One DistributedSampler & DataLoader per (simulated) rank
    samplers = [
        DistributedSampler(
            dataset,
            num_replicas=world_size,
            rank=rank,
            shuffle=True,
            seed=seed,
            drop_last=False,  # keep all samples; sampler will balance lengths across replicas
        )
        for rank in range(world_size)
    ]
    loaders = [
        DataLoader(
            dataset,
            batch_size=batch_size,
            sampler=samplers[rank],
            # Important: no 'shuffle=True' when using a sampler
        )
        for rank in range(world_size)
    ]

    for epoch in range(1, num_epochs + 1):
        model.train()
        # Coordinate epoch-wise shuffling across replicas
        for s in samplers:
            s.set_epoch(epoch)

        # Fresh iterators each epoch
        iters = [iter(loaders[r]) for r in range(world_size)]
        step, total_loss = 0, 0.0

        while True:
            # Gather one batch per rank; if any is exhausted, we end the epoch (sync semantics)
            batches = []
            for r in range(world_size):
                try:
                    batches.append(next(iters[r]))
                except StopIteration:
                    batches = []
                    break
            if not batches:
                break

            optimizer.zero_grad(set_to_none=True)

            # Per-step gradient averaging:
            # sum of grads / world_size  == allreduce-mean;
            # implemented by scaling each replica's loss by 1/world_size
            step_loss = 0.0
            for bx, by in batches:
                logits = model(bx)
                loss = criterion(logits, by) / world_size
                loss.backward()
                step_loss += loss.item()

            optimizer.step()

            total_loss += step_loss
            step += 1

        avg_step_loss = total_loss / max(step, 1)
        print(f"Epoch {epoch}: steps={step}, avg_step_loss={avg_step_loss:.4f}")

    return model


# ---------- Run ----------
if __name__ == "__main__":
    _ = train_sync_dp_with_distributedsampler(
        num_epochs=3,
        world_size=2,
        batch_size=16,
        lr=0.05,
        seed=123,
    )
