from common import *


def largest_n(d):
    for m in it.count():
        for n in it.count(1):
            s1 = sum([k for k in range(m, m+n)])
            s2 = sum([k for k in range(m+n, m+2*n)])

            if s2 - s1 == d:
                return n


print("Example: ", largest_n(9))
pans(largest_n(203401))
