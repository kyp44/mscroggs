import numpy as np
from common import *

# Sum number
s = 8


def N(m, s):
    """
    Recursive function
    """
    if m == 1:
        return 1
    else:
        return sum([N(m-1, j) for j in range(m-1, s-1+1)])


print("Recursive solution:", sum([N(m, s) for m in range(1, s+1)]))


# Direct, brute force solution
nums = []
for n in range(number([1 for i in range(s)]) + 1):
    ds = digits(n)
    if 0 not in ds and sum(ds) == s:
        nums.append(n)

pans(len(nums))
