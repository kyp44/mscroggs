from common import *

def S(n, N) :
    if N == 1 :
        return 1

    return sum([S(i-1, N-1) for i in range(N,n+1)])

print("Example:", S(5, 3))
pans(S(10,5))
