from numpy import sqrt
import itertools as it
from common import *

m = 14


def N(m):
    if m == 0:
        return 1
    elif m == 1:
        return 2
    else:
        return N(m-1) + N(m-2)


print("Recursive:", N(m))

phi = (1 + sqrt(5))/2
psi = (1 - sqrt(5))/2
def N(m): return (phi**(m+2) - psi**(m+2)) / sqrt(5)


print("Closed form:", N(m))

nums = []
for digs in it.product((1, 2), repeat=m):
    for i in range(len(digs)-1):
        if digs[i] == 2 and digs[i+1] == 2:
            break
    else:
        nums.append(number(digs))

pans(len(nums))
