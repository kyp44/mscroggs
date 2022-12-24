from scipy.special import binom
from common import *

n = 7

pans(sum([binom(n, k) * 3**(n - k) * (-1)**k for k in range(n+1)]))
