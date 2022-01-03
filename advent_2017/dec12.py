from common import *
import itertools as it
import sympy as sp

sums = (17, 7, 21, 11, 20, 14)
vals = dict(((n, []) for n in sums))
for x,y,z in it.combinations(range(1,9+1), 3) :
    s = x + y + z
    if s in sums :
        vals[s].append(set((x, y, z)))

c = vals[7][0]
for s in sums :
    print(s)
    if s == 17 :
        print([x for x in vals[s] if len(x & set((9, 7))) > 0 and len(x & c) == 0])
    elif s == 14 :
        print([x for x in vals[s] if 4 not in x and len(x & set((8,6))) > 0 and len(x & c) > 0])
    elif s in (11, 20) :
        print([x for x in vals[s] if len(x & c) > 0])
    else :
        print(vals[s])

pans(9*5*7)
