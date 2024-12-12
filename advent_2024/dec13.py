import numpy as np
from common import *

sol = np.array([[9, 9, 7],
                [4, 7, 0],
                [2, 3, 5]])


def across_1(sol): return sol[0, :]
def across_4(sol): return sol[1, :]
def across_5(sol): return sol[2, :]
def down_1(sol): return sol[:, 0]
def down_2(sol): return sol[:, 1]
def down_3(sol): return sol[:, 2]


def three_digs(a): return a[0] > 0


def clue_4a(sol): return anumber(across_4(sol)) == 2*anumber(across_5(sol))
def clue_1d(sol): return sum(down_1(sol)) == 15
def clue_2d(sol): return sum(down_2(sol)) == 19
def clue_3d(sol): return anumber(down_3(sol)) == 3*anumber(across_5(sol))


box_gen_solutions(
    3*[three_digs],
    3*[three_digs],
    sol,
    lambda s: anumber(s[0, :]),
    True,
    genchecks=[
        clue_4a,
        clue_1d,
        clue_2d,
        clue_3d,
    ],
    digits=False,
)
