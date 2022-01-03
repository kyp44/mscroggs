from common import *
import sympy as sp
from fractions import Fraction

fn = lambda x : Fraction(x,1)

Al = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 45],
      [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 11],
      [0, 0, 1, 1, 0, 0, 0, 0, -1, 0, 11],
      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 11],
      [1, 0, -1, 0, -1, 0, 0, 0, 0, 0, -11],
      [0, 1, 0, 1, 0, -1, 0, 0, 0, 0, 11],
      [0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 11]]

Af = [list(map(fn, r)) for r in Al]
A = sp.Matrix(Af)
print(A.rref()[0])

