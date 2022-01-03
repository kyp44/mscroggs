from common import *
from scipy.special import binom

N = lambda n : int(binom(n, 2)) + check_div(n*(n-1), 2)

print("Example:", N(3))
pans(N(29))
