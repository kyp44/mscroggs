from scipy.special import binom
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
