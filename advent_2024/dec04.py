from common import *

p = 13

for m in it.count(2):
    fs = list(factors(m))

    if product(fs) == p**len(fs):
        pans(m)
        break
