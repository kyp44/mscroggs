from common import *

N = 24

for m in it.count() :
    n = m*N
    ds = digits(n)
    #print(m, n, ds, sum(ds))
    if sum(ds) == N :
        print("Multiple:", m)
        pans(n)
        break
