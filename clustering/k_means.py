# type:ignore
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class KMeans:
    def __init__(self, n_clusters, max_iters=100):
        self.n_clusters = n_clusters
        self.max_iters = max_iters

    def fit(self, X):
        self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]

        for _ in range(self.max_iters):
            # Assign each data point to the nearest centroid
            labels = self._assign_labels(X)

            # update Centroids
            new_centroids = self._update_centroids(X, labels)

            # Check for convergence
            if np.all(self.centroids == new_centroids):
                break

            self.centroids = new_centroids

    def _assign_labels(self, X):
        diffs = X[:, None, :] - self.centroids[None, :, :]  # (N, K, D)
        dists = np.linalg.norm(diffs, axis=2)  # (N, K)

        # Assign labels based on the nearest centroid
        return np.argmin(dists, axis=1)

    def _update_centroids(self, X, labels):
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.n_clusters)])
        return new_centroids


# Load data
df1 = pd.read_csv("clustering/data_blob.csv")
my_data = df1.to_numpy()

# K-Means Clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(my_data)
labels = kmeans._assign_labels(my_data)  # Get cluster labels

# Plot clusters with colors
plt.scatter(my_data[:, 0], my_data[:, 1], c=labels, cmap="viridis", alpha=0.6)

# Plot centroids
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c="red", marker="X", s=200, label="Centroids")

# Labels & title
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means Clustering")
plt.legend()
plt.show()
