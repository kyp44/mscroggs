import numpy as np
from common import *


def e(k): return 18*k


def iter(N):
    for k in range(1, N+1):
        a = 10**k - 1
        b = a**3
        ds = digits(b)

        yield (k, a, b, ds)


for (k, a, b, ds) in iter(10):
    latex_row(k, a, b, len([d for d in ds if d == 9]))

    # print(f"{a}^3 = {b}", len([d for d in ds if d == 9]))

print()
for (k, _, _, ds) in iter(1000):
    if sum(ds) != e(k):
        print("Not valid!")
        break
else:
    print("Validated!")

print()
pans(e(55))
