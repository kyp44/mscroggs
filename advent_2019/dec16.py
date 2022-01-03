import numpy as np
from common import *

sol = np.array([[9,6,5],[2,8,3],[1,7,4]])

box_gen_solutions(
    (lambda r : np.median(r) == 6, lambda r : np.median(r) == 3, lambda r : np.mean(r) == 4),
    (lambda c : True, lambda c : np.mean(c) == 7, lambda c : max(c) - min(c) == 2),
    sol,
    lambda sol : anumber(sol[:,0]),
    True,
)
