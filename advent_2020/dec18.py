from common import *
from scipy.special import binom

nt = lambda nt, deg : int(binom(nt + deg - 1, deg))

print("Example:", nt(3, 3))
pans(nt(3, 26))
