from common import *

for n in range(800, 899+1) :
    ds = [int(d) for d in str(n)]

    if (n-1) % 9 != 0 :
        continue

    if sum(ds) % 5 != 0 :
        continue

    if len(set(ds)) != 2 :
        continue

    pans(n)
