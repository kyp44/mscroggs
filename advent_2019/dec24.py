import numpy as np
from common import *

sols = []
for n in range(100,1000) :
    ds = digits(n)
    if sum(ds) == np.product(ds) :
        sols.append(n)

print("Solutions:")
for n in sols :
    print(n)

pans(max(sols))
