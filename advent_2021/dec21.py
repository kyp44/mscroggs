from common import *
import numpy as np
import itertools as it

sol = np.array([[1, 4, 8], [2, 9, 3], [5, 7, 6]])

# Define check functions for this problem
odd = lambda a : anumber(a) % 2 == 1
prime = lambda a : len(factors(anumber(a))) == 2
def powerf(p) :
    def f(a) :
        n = anumber(a)
        for k in it.count(1) :
            s = k**p
            if s == n :
                return True
            if s > n :
                return False
    return f
mult11 = lambda a : anumber(a) % 11 == 0

box_gen_solutions(
    (lambda a : True, prime, powerf(2)),
    (powerf(3), odd, mult11),
    sol,
    lambda sol : anumber(sol[0,:]),
    True,
)
