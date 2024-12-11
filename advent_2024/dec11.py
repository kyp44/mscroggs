from scipy.special import binom
from common import *


def S(k, m): return sum([binom(m-1, l) * binom(2*k+1-m, l)
                         for l in range(k+1)])


print("Example:", S(2, 3))
pans(S(5, 5))
