import numpy as np
import itertools as it
from common import *

sol = np.array([[3, 7, 5], [6, 9, 1], [4, 8, 2]])


def cube(a): return anumber(a) in [k**3 for k in range(1, 12)]


def multf(m):
    return lambda a: anumber(a) % m == 0


def even_digits(a):
    return all([d % 2 == 0 for d in a])


def mult11(a): return anumber(a) % 11 == 0


box_gen_solutions(
    (multf(25), lambda a: True, even_digits),
    (multf(91), multf(7), cube),
    sol,
    lambda sol: anumber(sol[1, :]),
    True,
)
