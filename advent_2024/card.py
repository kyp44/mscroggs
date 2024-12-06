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
