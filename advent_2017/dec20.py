from common import *
import itertools as it

ns = list(range(0, 999+1))
cans = []

for a in it.count() :
    x = 10*a
    if x > 999 :
        break
    
    for b in it.count() :
        v = x + 27*b
        if v > 999 :
            break
        cans.append((v, a, b))
        if v in ns :
            ns.remove(v)

cans.sort()
for c in cans :
    print(c, 10*c[1] + 27*c[2])
pans(ns[-1])
