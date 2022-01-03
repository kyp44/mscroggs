import numpy as np
import itertools as it
from common import *

sol = np.array([[3, 8, 5], [4, 9, 7], [2, 1, 6]])

# Define check functions for this problem
cube = lambda a: anumber(a) in [k**3 for k in range(1, 12)]
def multf(m) :
    return lambda a : anumber(a) % m == 0

def powerf(p) :
    def f(a) :
        n = anumber(a)
        for k in it.count(1) :
            s = k**p
            if s == n :
                return True
            if s > n :
                return False
    return f
mult11 = lambda a : anumber(a) % 11 == 0

box_gen_solutions(
    (multf(5), multf(7), cube),
    (multf(9), multf(3), multf(4)),
    sol,
    lambda sol : anumber(sol[0,:]),
    True,
)
