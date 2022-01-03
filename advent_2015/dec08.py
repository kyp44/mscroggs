from common import *

maxnf = 0
maxn = None
for n in range(1, 1000000) :
    nfs = len(factors(n))
    if nfs > maxnf :
        maxn = n
        maxnf = nfs

print(maxn, "has", maxnf, "factors")
pans(maxn)
