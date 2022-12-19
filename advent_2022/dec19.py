from common import *
import itertools as it

x = None
for n in it.count(121):
    if len(factors(n)) == 16:
        x = n
        break

pans(x)
