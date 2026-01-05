from common import *

for n in range(400, 500):
    ds = digits(n)
    p = product(ds)
    if sum(ds) % 3 == 0 and p > 0 and cubic_number(p) is not None:
        pans(n)
        break
