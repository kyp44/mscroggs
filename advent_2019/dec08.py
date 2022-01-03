import itertools as it
from common import *

# Reasoned solution
nums = [10, 32, 54, 76, 98]
print("Analytical:", sum(nums))

# Brute force check
ms = -1
for ds in it.permutations("0123456789") :
    if set([int(ds[2*i+1]) for i in range(5)]) != {0,2,4,6,8} :
        continue
        
    s = sum([int(ds[2*i] + ds[2*i+1]) for i in range(5)])
    if s > ms :
        ms = s

pans(ms)
