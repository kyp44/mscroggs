from common import *

fs = factors(40)
s = 0
for n in range(1,39+1) :
    if n not in fs :
        s += n
pans(s)
