from common import *
import itertools as it

ds = tuple(range(1,9+1))

for x,y in it.combinations(ds, 2) :
    p = x*y
    if p % 27 == 0 :
        print(x, y, p)

pans(9*6*4)
