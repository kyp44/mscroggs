from common import *
import itertools as it

ns = list(range(100, 999+1))

for (a, b) in it.product(range(27+1), range(58+1)):
    v = 27*a + 17*b
    if v in ns:
        ns.remove(v)

pans(ns[-1])
