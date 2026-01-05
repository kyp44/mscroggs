from __future__ import annotations
from common import *

sol = np.array([[3, 2, 1],
                [9, 5, 8],
                [6, 7, 4]])

box_solutions(
    2025,
    16,
    sol,
    product,
    True,
)
