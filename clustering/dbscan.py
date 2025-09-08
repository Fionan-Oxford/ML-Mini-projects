# type: ignore
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# Produce some random blobs
rng = np.random.default_rng(42)

n, k, spread = 600, 5, 0.7
centers = rng.uniform(-1, 10, size=(k, 5))
y = rng.integers(0, k, size=n)
X = centers[y] + rng.normal(scale=spread, size=(n, 5))

# plt.scatter(X[:, 0], X[:, 1])
# plt.show()


class DBSCAN:
    """Simple implementation of DBSCAN"""

    def __init__(self, eps=0.9, min_samples=5):
        self.eps = eps
        self.min_samples = min_samples

    def fit(self, X):
        X = np.asarray(X, dtype=np.float32)
        n = X.shape[0]
        eps2 = self.eps * self.eps

        # Compute the distance from every point to every point
        # Euclidan distance is the sqare root of X2 - X1 squared and Y2 - Y1 Squared
        diffs = X[:, None, :] - X[None, :, :]
        dist2 = np.sum(diffs * diffs, axis=2)
        neighbours = dist2 <= eps2

        # Create core points
        counts = neighbours.sum(axis=1)
        core_mask = counts >= self.min_samples

        UNASSIGNED = -2
        labels = np.full(n, UNASSIGNED, dtype=np.int32)
        visited = np.zeros(n, dtype=bool)
        cluster_id = 0

        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True

            neigh_i = np.where(neighbours[i])[0]
            if neigh_i.size < self.min_samples:
                labels[i] = -1
                continue

            # Start a new cluster and expand it using BFS
            labels[i] = cluster_id
            queue = deque(neigh_i.tolist())
            in_queue = np.zeros(n, dtype=bool)
            in_queue[neigh_i] = True

            while queue:
                j = queue.pop()

                if not visited[j]:
                    visited[j] = True
                    neigh_j = np.where(neighbours[j])[0]
                    if neigh_j.size >= self.min_samples:
                        # add unseen neighbors to the queue
                        new_pts = neigh_j[~in_queue[neigh_j]]
                        in_queue[new_pts] = True
                        queue.extend(new_pts.tolist())

                # assign to cluster if unassigned or previously marked noise
                if labels[j] in (UNASSIGNED, -1):
                    labels[j] = cluster_id

            cluster_id += 1

        self.labels_ = labels
        self.core_sample_mask_ = core_mask
        self.n_clusters_ = int(labels.max() + 1) if (labels >= 0).any() else 0
        return self


db = DBSCAN(eps=0.9, min_samples=5).fit(X)
labels = db.labels_

# Plot
noise = labels == -1
plt.scatter(X[~noise, 0], X[~noise, 1], c=labels[~noise], s=16, cmap="tab10", alpha=0.8, label="clusters")
plt.scatter(X[noise, 0], X[noise, 1], c="lightgray", s=16, alpha=0.8, label="noise")
cores = db.core_sample_mask_ & ~noise
plt.scatter(X[cores, 0], X[cores, 1], facecolors="none", edgecolors="k", s=60, linewidth=1, label="core")
plt.axis("equal")
plt.title("DBSCAN (NumPy-only)")
plt.legend()
plt.show()
