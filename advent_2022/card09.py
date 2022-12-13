from copy import copy
from common import *

nums = []
for n in range(10000, 99999+1):
    ds = digits(n)

    # Try removing all digits
    for i in range(len(ds)):
        ms = copy(ds)
        del ms[i]
        m = number(ms)
        if n + m == 96158:
            nums.append((n, m))

mt = max(nums, key=lambda t: t[0])
print(mt)
pans(mt[0])
