from scipy.special import binom
from scipy.stats import gmean
from common import *

maxp = 0

prob(1)
for ds in it.product(range(1, 4+1), repeat=4):
    a = number(ds[:2])
    b = number(ds[2:])
    p = a*b

    if p > maxp:
        maxp = p
pans(maxp)

prob(3)
def S(a, b, n): return sum([binom(n, k) * a**(n-k) * b**k for k in range(n+1)])


print("Example:", S(2, 3, 2))
print("Wolfram Alpha:", sum([900, 300, 25]))
pans(S(30, 5, 2))

prob(4)
pans(S(2, 1, 11))

prob(5)
pans(gmean(list(factors(41306329))))

prob(6)
b = 92**2
print("Geometric mean check:", gmean(list(factors(b))))
pans(b)

prob(7)
pans(sum(factors(7**4)))

prob(8)
count = 0
for k in it.count(1):
    n = k**2
    if n > 28988500000:
        break
    count += 1
pans(count)

prob(9)
n = 365
def sf(a): return sum([k for k in range(a, a+n)])


pans(sf(500+n) - sf(500))
