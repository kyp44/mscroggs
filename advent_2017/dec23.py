from common import *

s = 0

for d in range(1,8+1) :
    for g in range(1, d+1) :
        s += g

print(s)

N = 8
pans(N*(N+1)*(N+2) / 6)
