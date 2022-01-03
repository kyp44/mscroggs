from common import *
v = 1

for n in range(1,23+1) :
    r = []
    for k in range(n) :
        r.append(v)
        v += 2
    print(r)

pans(sum(r) // 23)
