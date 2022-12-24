from common import *

ns = []
for s in range(1, 27+1):
    n = s*(s + 10)
    S = sum(digits(n))

    latex_row(s, n, S)
    if s == S:
        ns.append(n)

print(sorted(ns))
pans(min(ns))
