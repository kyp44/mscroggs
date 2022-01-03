import numpy as np
from common import *

# Number of tokens
N = 2

# Grid size
m, n = 2, 21

# All grid coordinates
gcs = list(it.product(range(m), range(n)))

# Checks whether a set of token coordinates is valid
def valid(tcs) :
    # Pick out every pair of coords
    for t1, t2 in it.combinations(tcs, 2) :
        if np.linalg.norm(np.array(t1) - np.array(t2)) < 2 :
            return False

    return True

# Pick out all combinations of N tokens
print("Brute force:", len([1 for tcs in it.combinations(gcs, N) if valid(tcs)]))

# Analytical
pans(2*(n-2)*(n-1))
