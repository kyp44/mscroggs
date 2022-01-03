from common import *
import itertools as it

pds = set([])

def product(it) :
    p = 1
    for v in it :
        p *= v
    return p

for tup in it.combinations_with_replacement((2,3,4), 9) :
    pds.add(product(tup))

spds = sorted(list(pds))
ans = spds[1]
print(spds)
print(2**8 * 3, ans)


print("Factors of the answer for the clue:")
for n in range(1, 24+1) :
    if ans % n == 0 :
        print(n)
