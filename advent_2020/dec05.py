import numpy as np
from common import *

Ns = 6
b = np.array([200, 521])
A = np.array([[1, 1], [6, -1]])
n, i = [int(v) for v in np.linalg.solve(A, b)]
print(n, i)
pans(n)
