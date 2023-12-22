from copy import copy
from common import *
from common.probs import factorial_minus


prob(1)
pans(factorial_minus(1))

prob(2)
pans(factorial_minus(44))

prob(7)
# n-digit numbers
n = 3
# Number of digits to allow
d = 5
valid_digs = set(range(1, d+1))
cnt = 0
for k in range(10**(n-1), 10**n):
    ds = digits(k)
    if set(ds).issubset(valid_digs):
        if len([x for x in ds if x == 1]) == n-1:
            cnt += 1


def N(n):
    if n == 1:
        return d-1
    else:
        return d-1 + N(n-1)


print("Recursive:", N(n))
print("Formulat:", n*(d-1))
pans(cnt)
