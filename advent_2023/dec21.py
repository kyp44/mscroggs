from common import *


def N(n, k): return binom(k + n - 1, n)


pans(N(20, 3))
