
from common import *

def N(m, n=2, s=0, ns=[]) :
    # Base cases
    if m == 0 :
        if s == 1 :
            print(ns)
            return 1
        else :
            return 0
    elif s >= 1 :
        return 0
    
    # Recurse
    return sum([N(m - 1, nn, s + frc(1,nn), ns + [nn]) for nn in range(n, np.floor(frc(m) / (1 - s)) + 1)])
    
pans(N(5))
