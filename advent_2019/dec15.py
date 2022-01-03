import itertools as it
from common import *

def mults(n) :
    ways = [(n,)]
    
    for f1 in range(2, n // 2 + 1) :
        if n % f1 == 0 :
            f2 = n // f1
            ways1 = mults(f1)
            ways2 = mults(f2)

            for w1, w2 in it.product(ways1, ways2) :
                a = tuple(sorted(tuple(w1) + tuple(w2)))
                if a not in ways :
                    ways.append(a)

    return tuple(sorted(ways))


ways = mults(30030)
print("Ways:")
for w in ways :
    print(w)
pans(len(ways))
