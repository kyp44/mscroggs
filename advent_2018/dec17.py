from common import *
import itertools as it

s = 0

for x,y in it.product(range(1,9+1), repeat=2) :
    if x < y :
        s += x
    else :
        s += y

pans(s)
