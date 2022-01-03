from common import *
N = 10

ns = [1, 1]

for i in range(2, N+1) :
    ns.append(ns[i-1] + 2*ns[i-2])

print(ns)
pans(ns[9])
