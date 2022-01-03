import numpy as np
from common import *

nums = []
for n in range(100, 1000) :
    for b in range(3, 9+1) :
        if "2" in np.base_repr(n, b) :
            break
    else :
        nums.append(n)
        """
        print("---------", n)
        for b in range(3, 9+1) :
            print(b, np.base_repr(n, b))
        """

print("Solutions:")
for n in nums :
    print(n)

pans(min(nums))
