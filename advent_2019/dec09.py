import numpy as np
from common import *

sol = np.array([[5,7,1],[2,8,4],[3,9,6]])

# Define check functions for this problem
oddf = lambda a : all([v % 2 == 1 for v in a])
evenf = lambda a : all([v % 2 == 0 for v in a])
mult3 = lambda a : all([v % 3 == 0 for v in a])
great6 = lambda a : all([v > 6 for v in a])
nonp = lambda a : all([v in (1,4,6,8,9) for v in a])

box_gen_solutions(
    (oddf, evenf, mult3),
    (lambda n : True, great6, nonp),
    sol,
    lambda sol : anumber(sol[:,0]),
    True,
)
