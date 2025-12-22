from common import *

num = product([PrimeFactors(i+1)**e for i, e in enumerate(range(500, 0, -1))])

for n in range(100, 1000):
    npf = PrimeFactors(n).factorial()

    if num.ismultiple(npf):
        if (num / npf).is_square():
            pans(n)
            break
