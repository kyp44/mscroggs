import numpy as np
from common import *

sol = np.array([[1, 2, 5],
                [2, 5, 6],
                [1, 0, 4]])


def cube(a): return anumber(a) in [k**3 for k in range(1, 12)]
def square(a): return anumber(a) in [k**2 for k in range(1, 50)]


def multf(m):
    return lambda a: anumber(a) % m == 0


ver = [
    cube(sol[0, :]),
    square(sol[1, :]),
    multf(13)(sol[2, :]),
    square(sol[:, 0]),
    anumber(sol[:, 1]) == 2*anumber(sol[0, :]),
]
print("Verified:", all(ver))
pans(anumber(sol[:, 2]))
