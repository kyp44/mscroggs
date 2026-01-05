from __future__ import annotations
from common import *


sol = np.array([[1, 7, 5],
                [3, 5, 0],
                [-1, 3, 5]])


def across_1(sol): return sol[0, :]
def across_4(sol): return sol[1, :]
def across_5(sol): return sol[2, 1:]
def down_1(sol): return sol[:2, 0]
def down_2(sol): return sol[:, 1]
def down_3(sol): return sol[:, 2]


def nonzero_first_dig(a): return a[0] > 0
def nonzero_second_dig(a): return a[1] > 0


def clue_4a(sol): return anumber(across_4(sol)) == 2*anumber(across_1(sol))
def clue_5a(sol): return anumber(across_5(sol)) == product(across_1(sol))
def clue_1d(sol): return anumber(down_1(sol)) == sum(across_1(sol))
def clue_2d(sol): return anumber(down_2(sol)) in [
    anumber(ds) + 2 for ds in it.permutations(across_1(sol))]


def clue_3d(sol): return anumber(down_3(sol)) in [101*k for k in range(1, 10)]


box_gen_solutions(
    [nonzero_first_dig, nonzero_first_dig, nonzero_second_dig],
    3*[nonzero_first_dig],
    sol,
    lambda s: anumber(across_1(s)),
    # This takes too long to run
    False,
    genchecks=[
        clue_4a,
        clue_5a,
        clue_1d,
        clue_2d,
        clue_3d
    ],
    digits=False,
)
