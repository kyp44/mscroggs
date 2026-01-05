from __future__ import annotations
from common import *

ns = []
for n in range(100, 1000):
    ds = digits(n)
    ds.reverse()

    if n + number(ds) == 968:
        ns.append(n)

pans(min(ns))
