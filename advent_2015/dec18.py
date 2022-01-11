import numpy as np
import itertools as it
from common import *

sol = np.array([[8, 9, 1], [3, 7, 2], [4, 6, 5]])

# Define check functions for this problem
def multf(m) :
    return lambda a : anumber(a) % m == 0
cube = lambda a : anumber(a) in [n**3 for n in range(1, 10+1)]

box_gen_solutions(
    (multf(9), multf(3), multf(5)),
    (multf(6), multf(4), cube),
    sol,
    lambda sol : anumber(sol[:,0]),
    True,
)
