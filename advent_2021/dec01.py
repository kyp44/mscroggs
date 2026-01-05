import itertools as it
from common import *

m = 2
x = 2**m * 11**m
fs = factors(x)
print("Factors:", fs)
print("Verification:", product(fs), 22**len(fs))

pans(x)
