import numpy as np
import itertools as it
from common import *

sol = np.array([[3, 8, 5], [4, 9, 7], [2, 1, 6]])

# Define check functions for this problem
even = lambda a: anumber(a) % 2 == 0
odd = lambda a: anumber(a) % 2 == 1
even_digs = lambda a : all([d % 2 == 0 for d in a])

box_gen_solutions(
    (odd, even_digs, lambda a : True),
    (even, odd, lambda a : True),
    sol,
    lambda sol : max([anumber(r) for r in sol] + [anumber(c) for c in sol.transpose()]),
    False,
    genchecks=[
        lambda sol : anumber(sol[0,:]) + anumber(sol[1,:]) == anumber(sol[2,:]),
        lambda sol : anumber(sol[:,0]) + anumber(sol[:,1]) == anumber(sol[:,2]),
    ],
)

for a, b in it.product((1, 3, 5, 7, 9), (2, 4, 6, 8)) :
    c = a + b
    if c < 10 :
        print(a, b, c)
