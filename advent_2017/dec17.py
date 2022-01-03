from common import *
import itertools as it

def digs(n) :
    return [int(c) for c in str(n)]

def from_digs(ds) :
    return int("".join([str(d) for d in ds]))

b = 10

ss = []
while True :
    v = b**2
    if len(str(v)) > 3 :
        break
    ss.append(v)
    b += 1

for ns in it.combinations(ss, 3) :
    if len(set.union(*[set(digs(n)) for n in ns])) == 9 :
        break

for p in it.permutations(ns) :
    vn = lambda k : from_digs([digs(v)[k] for v in p])
    if vn(0) % 7 == 0 and vn(1) % 4 == 0 :
        print(p)
        pans(vn(2))
