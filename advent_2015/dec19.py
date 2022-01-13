from common import *

def N(Nl, ns=[]) :
    # Base cases
    s = sum([frc(1, n) for n in ns])
    if Nl == 0 :
        if s == 1 :
            print(ns)
            return 1
        else :
            return 0
    elif s >= 1 :
        return 0
    
    # Recurse
    cnt = 0
    a = 2 if len(ns) == 0 else ns[-1]
    for n in range(a, np.floor(frc(Nl) / (1 - s)) + 1) :
        cnt += N(Nl - 1, ns + [n])
    return cnt

    
pans(N(5))
