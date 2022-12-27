from common import *

for n in range(100, 1000):
    ds = digits(n)

    if ds[2] != 8:
        continue

    if n % 9 != 1:
        continue

    if len(set(ds)) != 2:
        continue

    if sum(ds) % 5 != 0:
        continue

    pans(n)
