from common import *
import numpy as np

k = 1
n = 0
while True :
    v = 2*k
    if v > 25 :
        break
    print(v)
    n += 1
    k += 2

ans = [142, 106, 249, 819, 154]

t = sum(ans) / (n-1)
print(t)
pans(np.mean(ans + [t]))
