from __future__ import annotations
from common import *

p = 29
for n in it.count(100):
    if PrimeFactors(n).is_perfect_power() and PrimeFactors(n + p).is_perfect_power():
        pans(n)
        break
