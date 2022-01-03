from common import *

for n in range(100, 1000) :
    ds = [int(d) for d in str(n)]

    s = sum(ds)
    if n == s*(s+10) :
        pans(n)
        break
