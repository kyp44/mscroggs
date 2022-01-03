from common import *
import itertools as it

def fact(n) :
    v = n
    fs = []
    for k in range(1, 9+1) :
        if v % k == 0 :
            fs.append(k)
    return fs

vs = (90, 84, 48, 64, 90, 63)
for v in vs :
    print(v, fact(v))

ns = [int("".join([str(d) for d in p])) for p in it.permutations((2,8,6))]
pans(min(ns))
