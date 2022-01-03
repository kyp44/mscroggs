from common import *

N = 1000
bad_ds = set((0,1,2,3))

c = 0
for n in range(10,N+1) :
    ds = set([int(d) for d in str(n)])
    if len(bad_ds & ds) == 0 :
        c += 1
pans(c)
