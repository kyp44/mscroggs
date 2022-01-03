import numpy as np
import itertools as it
from common import *

sol = np.array([[2,1,-1,-1],
                [5,2,1,-1],
                [-1,2,1,1],
                [-1,-1,9,1]])
print("Deduced solution:")
print(sol)

solarr = lambda sol : {"1A" : sol[0,0:2],
                       "3A" : sol[1,0:3],
                       "5A" : sol[2,1:],
                       "7A" : sol[3,2:],
                       "1D" : sol[0:2,0],
                       "2D" : sol[0:3,1],
                       "4D" : sol[1:,2],
                       "6D" : sol[2:,3]}

# Converts digit array to integer
num = lambda arr : int("".join([str(d) for d in arr]))

"""
Checks that the number lab satisfies
the check but no other numbers do.
f should take a number array and return
boolean whether the condition is satisfied.
"""
def check(lab, f, sola) :
    for k in sola.keys() :
        if k == lab :
            if not f(sola[k]) :
                return False
        else :
            if f(sola[k]) :
                return False

    return True

"""
Checks every condition for a solution
matrix.
"""
def checkall(sol) :
    # Boolean list of check results
    res = []

    sola = solarr(sol)

    # Check the conditions
    res.append(check("1A", lambda a : num(a) % 3 == 0, sola))
    res.append(check("3A", lambda a : num(a) > 300, sola))
    res.append(check("7A", lambda a : num(a) % 13 == 0, sola))
    res.append(check("1D", lambda a : np.sqrt(num(a)) == int(np.sqrt(num(a))), sola))
    res.append(check("2D", lambda a : np.prod(a) == 4, sola))
    res.append(check("4D", lambda a : np.sum(a) == 11, sola))
    res.append(check("6D", lambda a : num(a) < 20, sola))

    return np.all(res)

print("Solution verified:", checkall(sol))
pans(num(solarr(sol)["5A"]))

# Use brute force to search for a solution
print("Brute force solutions:")

def pfunc(nums) :
    s = -1*np.ones((4,4), dtype=int)
    s[0,0] = nums[0]
    s[0,1] = nums[1]
    s[1,0] = nums[2]
    s[1,1] = nums[3]
    s[1,2] = nums[4]
    s[2,1] = nums[5]
    s[2,2] = nums[6]
    s[2,3] = nums[7]
    s[3,2] = nums[8]
    s[3,3] = nums[9]

    if checkall(s) :
        print(s)

for nums in it.product(range(9+1), repeat=10) :
    pfunc(nums)
