from common import *
from scipy.special import binom
import itertools as it

N = 10

c = 0
for s in it.product(("A", "B"), repeat=10) :
    if len([v for v in s if v == "A"]) >= 3 :
        c += 1

print(c)
pans(sum([int(binom(N, k)) for k in range(3,N+1)]))
