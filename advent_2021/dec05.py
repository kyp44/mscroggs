from pylab import *
import itertools as it
from common import *

# Perimeter
p = 50

bs = linspace(0, p/2, 500)
f = lambda b : b * sqrt(p * (p - 2*b)) / 4

bmax = p/3
fmax = f(bmax)
print("fmax:", fmax)

pans(2 * int(floor(fmax)))
