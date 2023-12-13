from common import *

k = 8
a = 2*k + 1


def Sr(r): return sum(range(r, (a - r + 1) + 1))


print((k+1)**3)
pans(sum([Sr(r) for r in range(1, k+1 + 1)]))
