from common import *
import itertools as it

anss = [563, 435, 798, 140, 414, 819, 691, 768, 449, 171, 811, 419,
        512, 415, 387, 543, 179, 799, 128, 287, 000, 191, 771]

for (n, m) in it.product(anss, anss) :
    if n > m :
        (n, m) = (m, n)

    a = n + 191
    if a == m - 100 :
        pans(a)
        break
