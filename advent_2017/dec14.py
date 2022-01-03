from common import *
import itertools as it

N = 13

c = 0
for s in range(1, N+1) :
    for x,y in it.product(range(N-s+1), repeat=2) :
        c += 1
print(c)
pans(N*(N+1)*(2*N+1) // 6)
