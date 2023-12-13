from common import *

s = 0
for n in range(100, 1000+1):
    if sum(digits(n)) % 2 == 0:
        s += 1

pans(s)
