from common import *
from pylab import *
import itertools as it

anss = [563, 435, 798, 140, 414, 819, 691, 768, 449, 171, 811, 419,
        512, 415, 387, 543, 179, 799, 128, 287, 1, 191, 771, 319]

adt = [n for n in anss if n % 3 == 0]

for m in range(1, 10) :
    a = (len(adt) + 1)*193*m - sum(adt)
    if 99 < a < 1000 :
        pans(a)
        break

nadt = adt + [a]
print(int(mean(nadt)) % 193)
