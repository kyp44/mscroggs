from common import *
import numpy as np

for n in range(100, 999+1) :
    ds = [int(d) for d in str(n)]

    s = sum(ds)
    p = np.prod(ds)

    if s == p :
        print(n, s, p)
        break
