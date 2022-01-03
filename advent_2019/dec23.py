import numpy as np
from common import *

sol = np.array([[8,1,6],[7,2,9],[4,5,3]])

# Define check functions for this problem
odd = lambda a : anumber(a) % 2 == 1
mult3 = lambda a : anumber(a) % 3 == 0
mult4 = lambda a : anumber(a) % 4 == 0
cube = lambda a : anumber(a) in [x**3 for x in range(12)]

box_gen_solutions(
    (mult4, cube, mult3),
    (lambda a : True, cube, odd),
    sol,
    lambda sol : anumber(sol[:,0]),
    True,
)
