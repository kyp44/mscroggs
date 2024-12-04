from common import *

N = 888

# Products of dice
ps = []

# Calculate products of possible dice rolls
for ds in it.combinations(range(1, N+1), r=2):
    ps.append(product(ds))

# Find the smallest even integer not in the list
for k in it.count(1):
    n = 2*k

    if n not in ps:
        pans(n)
        break
