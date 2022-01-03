import itertools as it
from common import *

gN = 20

tn = lambda N, n : int(N*(N+2*n-1)/2)

print(tn(gN, gN))
    
for N,n in it.product(range(1,gN+1), repeat=2) :
    if tn(N,n) == 208 :
        # Found out our N and n
        print("N =", N)
        print("n =", n)
        pans(tn(N,n+1))
