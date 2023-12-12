from common import *
from math import ceil


def N(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return N(n-1) + N(n-2)


for n in range(1, 12+1):
    print(n, "&", N(n), "\\\\")

pans(N(12))
