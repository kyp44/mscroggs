from common import *

for n in range(100, 1000):
    s = sum(digits(n))
    if n == s*(s+10):
        pans(n)
        break
