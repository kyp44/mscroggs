from common import *
from scipy.special import binom

r = 8-1

pans(sum([int(binom(r, k)) for k in range(r+1)]))
