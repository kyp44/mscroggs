from scipy.special import binom
from scipy.stats import gmean
from common import *

prob(1)
nss = [(number(ds[:2]), number(ds[2:]))
       for ds in it.permutations(range(1, 4+1))]
(x, y) = max(nss, key=lambda ns: ns[0] * ns[1])
print("Best numbers:", x, y)
pans(x * y)

prob(2)
nss = [(number(ds[:2]), number(ds[2:]))
       for ds in it.permutations(range(0, 9+1))]
(x, y) = max(nss, key=lambda ns: ns[0] * ns[1])
print("Best numbers:", x, y)
pans(x * y)

prob(3)
def S(a, b, n): return sum([binom(n, k) * a**(n-k) * b**k for k in range(n+1)])


print("Example:", S(2, 3, 2))
print("Wolfram Alpha:", sum([900, 300, 25]))
pans(S(30, 5, 2))

prob(4)
pans(S(2, 1, 11))

prob(5)
pans(gmean(factors(41306329)))

prob(6)
b = 92**2
print("Geometric mean check:", gmean(factors(b)))
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
