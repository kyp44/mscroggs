from common import *
from itertools import count


def largest_n(d):
    for m in count():
        for n in count(1):
            s1 = sum([k for k in range(m, m+n)])
            s2 = sum([k for k in range(m+n, m+2*n)])

            if s2 - s1 == d:
                return n


print("Example: ", largest_n(9))
pans(largest_n(203401))
