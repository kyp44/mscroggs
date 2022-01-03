from common import *

def N(m) :
    for n in it.count(1) :
        if m * sum(digits(n)) == n :
            return n

print("Example:", N(11))
pans(N(48))
