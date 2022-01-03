import itertools as it
import numpy as np
from common import *

cnt = 0

for pns in it.combinations(range(28), 3) :
    # Points in complex unit circle
    pts = [np.exp(1j*2*np.pi*n/28) for n in pns]

    # Lenths between points
    lens = [np.abs(a - b) for a,b in it.combinations(pts, 2)]

    # Check whether two lengths are the same
    for la,lb in it.combinations(lens, 2) :
        if abs(la - lb) < 1e-8 :
            cnt += 1
            break

pans(cnt)
