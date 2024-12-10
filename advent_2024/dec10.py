from common import *

s = 0
for n in range(10, 100+1):
    ds = digits(n)

    if ds == ds[::-1]:
        print(n)
        s += n

print()
pans(s)
