from common import *

for N in range(4, 22+1) :
    ss = [n**2 for n in range(1, N+1)]
    maxs = max(ss)
    ns = [sum([b*s for b, s in zip(bs, ss)]) for bs in it.product(range(1+1), repeat=N)]
    #print(len(set(ns)), 2**N)
    ns = set([n for n in ns if n <= maxs])
    maxn = max(set(range(1, maxs+1)) - ns)
    print(N, maxn)
pans(maxn)
