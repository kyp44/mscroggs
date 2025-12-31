from __future__ import annotations
from common import *

ns = [n for n in range(100, 1000) if sum(
    map(lambda x: x**3, digits(n))) == n]

print(ns)
pans(ns[-1])
