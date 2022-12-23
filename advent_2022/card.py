from copy import copy
from common import *


def prob(n):
    sep = "".join(["-" for i in range(20)])
    print(sep + " Problem " + str(n) + " " + sep)


prob(6)
digital_sums(7, num_digs=4, analytical=lambda s: (s**3 - 6*s**2 + 11*s - 6)/6)

prob(7)
digital_sums(7)

prob(9)
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

for mt in nums:
    print(mt)

mt = max(nums, key=lambda t: t[0])
pans(mt[0])
