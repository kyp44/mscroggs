from common import *
import numpy as np

A = np.array([[1, 1, 0],
              [1, 0, 1],
              [0, 1, 1]])
b = np.array([99, 83, 102])

x = np.linalg.solve(A, b)
print(x)
pans(sum(x))
