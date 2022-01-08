import numpy as np
import itertools as it
from common import *

sol = np.array([[1, 5, 7], [4, 8, 2], [6, 3, 9]])

# Define check functions for this problem
even = lambda a: anumber(a) % 2 == 0
odd = lambda a: anumber(a) % 2 == 1
even_digs = lambda a : all([d % 2 == 0 for d in a])

box_gen_solutions(
    (odd, even_digs, lambda a : True),
    (even, odd, lambda a : True),
    sol,
    lambda sol : max([anumber(r) for r in sol] + [anumber(c) for c in sol.transpose()]),
    True,
    genchecks=[
        lambda sol : anumber(sol[0,:]) + anumber(sol[1,:]) == anumber(sol[2,:]),
        lambda sol : anumber(sol[:,0]) + anumber(sol[:,1]) == anumber(sol[:,2]),
    ],
)
