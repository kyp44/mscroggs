from common import *

for n in range(100, 999+1) :
    ds = [int(d) for d in str(n)]

    if sum(ds) == 25 :
        pans(n)
        break
