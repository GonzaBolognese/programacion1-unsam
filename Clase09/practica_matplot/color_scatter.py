import numpy as np
import matplotlib.pyplot as plt


n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)

T = np.arctan2(Y, X)


plt.scatter(X, Y, c=T, s=40, cmap='viridis', alpha=0.6)

plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.show()
