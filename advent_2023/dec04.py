from common import *
from math import factorial as fact

a = 123
ans = -1

for n in range(1, 1000):
    x = fact(n) - a
    y = n - a

    if y != 0 and x % y == 0:
        ans = n

pans(ans)
