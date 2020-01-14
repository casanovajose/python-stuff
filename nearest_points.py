import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set()
rand = np.random.RandomState(42)

X = rand.rand(10, 2)
print("X = ", X )
# plt.scatter(X[:, 0], X[:, 1])

differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
sq_differences = differences ** 2

dist_sq = sq_differences.sum(-1)

print("diagonal ", dist_sq.diagonal())

nearest = np.argsort(dist_sq, axis=1)
print("Nearest ", nearest)

K = 1
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)

plt.scatter(X[:, 0], X[:, 1], s=100)

for i in range(X.shape[0]):
  for j in nearest_partition[i, : K+1]:
    plt.plot(*zip(X[j], X[i]), color="black")