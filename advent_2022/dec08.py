import numpy as np
from fractions import Fraction as frc
from common import *

a = 840
cs = [1, -7, -27, 175, 218, -840]
fs = factors(a)

print("Number of factors of", str(a) + ":", len(fs))

roots = []
for x in fs:
    # Need to try both positive and negative roots
    if np.polyval(cs, x) == 0:
        roots.append(x)
    if np.polyval(cs, -x) == 0:
        roots.append(-x)

print("Roots:", sorted(roots))
