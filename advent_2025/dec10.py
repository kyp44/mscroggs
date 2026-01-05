from __future__ import annotations
from common import *


def lowest_with_factors(nf):
    for n in it.count():
        fs = factors(n)
        if 2 not in fs and len(factors(n)) == nf:
            return n


print("Example:", lowest_with_factors(15))
pans(lowest_with_factors(16))
