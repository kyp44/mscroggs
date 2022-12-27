from common import *

ns = []
for n in range(100, 999+1) :
    if (n-3) % 7 !=  0 :
        ns.append(n)
pans(len(ns))
#print(ns)
