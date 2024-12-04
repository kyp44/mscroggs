from common import *

p = 13

ms = []
for m in range(1, 1000):
    fs = list(factors(m))

    if product(fs) == p**len(fs):
        ms.append(m)

print(ms)
pans(ms[0])
