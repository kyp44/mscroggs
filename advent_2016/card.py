from common import *
import itertools as it
from pylab import *


def digs(n): return [int(d) for d in str(n)]
def rev(n): return int("".join(reversed(str(n))))


# Maximum value that is 222222222 in base 3
maxn = sum([2*3**n for n in range(0, 9+1)])


def facts(n):
    fs = []
    for k in range(1, int(n/2)+1):
        if n % k == 0:
            fs.append(k)
    fs.append(n)
    return fs


def square(n):
    sr = sqrt(n)
    return sr - int(sr) == 0


def outerp(av, bv): return [a*b for (a, b) in it.product(av, bv)]


prob(1)
for n in it.count(2):
    s = n**2
    if (sum(digs(s)) == n):
        pans(s)
        break

prob(2)
for n in it.count(2):
    s = n**2
    sf = sum(factors(s))
    if square(sf):
        pans(s)
        break

prob(3)
ns = list(range(0, maxn+1))
for (n, m) in it.product(range(int(ceil(maxn/23))), range(int(ceil(maxn/17)))):
    nn = 23*n + 17*m
    if nn in ns:
        ns.remove(nn)
pans(ns[-1])

prob(4)
n = 642
a = n - rev(n)
pans(a + rev(a))

prob(5)
ns = []
badd = set((0, 1, 2, 3, 4, 5, 6))
for n in range(int(10e6)+1):
    if len(badd.intersection(set(digs(n)))) == 0:
        ns.append(n)
pans(len(ns))

prob(6)
for m in range(1, 57+1):
    n = 249*m
    if n % 57 == 0:
        pans(n)
        break

prob(7)
pans(sum([n for n in range(66) if n % 2 == 1]))

prob(8)
t = sum([k for k in range(1, 40+1)])
pans(4*t - 1)

prob(9)
n = 2
m = 3
fn = [2**k for k in range(756+1)]
fm = [3**k for k in range(12+1)]
f = set(outerp(fn, fm))
pans(len(f))

prob(10)
p = 13204
pans(int(p/2 + p/2 + 1))

prob(11)
pans(27*26)

prob(12)
ns = []
for k in range(1, maxn+1):
    if 27*k % (27 + k) == 0:
        ns.append(k)
pans(ns[-1])
