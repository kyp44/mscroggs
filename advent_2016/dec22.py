from common import *

pns = []

for n in range(111, 11111+1) :
    rn = int("".join(reversed(str(n))))

    if rn == n :
        pns.append(n)

pans(len(pns))
