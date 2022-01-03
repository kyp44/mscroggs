from common import *
import itertools as it

gs = []
for seq in it.product(range(3), repeat=6) :
    for i in range(1,5+1) :
        if seq[i-1] + seq[i] >= 3 :
            break
    else :
        gs.append(seq)

for s in gs :
    print(s)

pans(len(gs))
