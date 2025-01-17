import numpy as np
from math import factorial
from math import gcd
from common import *

prob(1)
N = 10000
cnt = 0
for n in range(1, N+1):
    s = str(n)
    cnt += len([d for d in s if d == "1"])

pans(cnt)

prob(2)
a = sum([n for n in range(86) if n % 2 == 1])
pans(a)

prob(4)
N = 130404

pans(N+1)

prob(5)
rs = 60153
pans(2*rs)

prob(6)


def f(n):
    if n < 1:
        raise ValueError("invalid parameter: " + str(n))
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f(n-1) + f(n-2)


pans(f(28))

prob(7)


def lcm(a, b):
    return a*b // gcd(a, b)


pans(lcm(1025, 835))

prob(8)
pans(count_ending_zeros(factorial(245)))

prob(9)
for n in range(10**5, 10**6):
    for dd in range(6+1):
        ds = digits(n)
        if dd > len(ds)-1:
            continue
        ds.pop(dd)
        nd = number(ds)
        if n + nd == 334877:
            pans(n)
