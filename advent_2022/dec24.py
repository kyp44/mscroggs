from scipy.special import binom
from common import *


def S(a, b, n): return sum([binom(n, k) * a**(n-k) * b**k for k in range(n+1)])


pans(S(3, -1, 7))
