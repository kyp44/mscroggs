from common import *
from pylab import *
import itertools as it
from math import gcd

wait = True


def lcm(a, b):
    return abs(a * b) / gcd(a, b) if a and b else 0


def facts(n):
    fs = []
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            fs.append(k)
    fs.append(n)
    return fs


def fint(x):
    return int(round(x))


prob(1)
n = 1000
while True:
    ds = [int(d) for d in str(n)]
    if sum(ds) == 6:
        pans(n)
        break
    n += 1

prob(2)
a = 152560
b = 114420
pans(int(sqrt(a**2 + b**2)))

prob(3)
pans(int(lcm(1346, 196)))

prob(4)
# This formula was derived as part of a 2018 advent calendar problem
n = 696 // 2
pans((n+1)**2)

prob(5)
# Similar to problem in 2018 advent calendar problem
"""
c = 0
for n in range(100,10000+1) :
    for d in [int(ds) for ds in str(n)] :
        if d in (0,1,2,3) :
            break
    else :
        c += 1
print(c)
"""
pans(6**4 + 6**3)

prob(6)
pans(14*20*10*40)

prob(7)
N = 16020308
p = N // 2
pans(2*p + 1)

prob(8)
if wait:
    s = 18745225
    for n in range(s//2, s+1):
        ns = str(n)
        m = int(ns[:-1])
        if n + m == s:
            break
    pans(n)

prob(9)
m = 13
n = 119
pans((m-1)*n - m)

prob(10)
(n, m) = (7, 6)
c = 0
for seq in it.product((0, 1), repeat=(n+m)):
    if sum(seq) == m:
        # print(seq)
        c += 1
pans(c)
