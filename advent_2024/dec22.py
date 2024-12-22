from common import *

sol = np.array([[9, 3, 4],
                [7, 5, 6],
                [1, 2, 8]])

box_solutions(
    2024,
    22,
    sol,
    lambda xs: number(sorted(xs)),
    True,
)
