from common import *

nd = 4

ss = set([])

for n in range(10**(nd-1), 10**nd) :
    ds = [int(d) for d in str(n)]
    ss.add(sum(ds))

print(ss)
print(len(ss))
