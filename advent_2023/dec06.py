from common import *
from math import ceil


def A(n, k):
    if n == 0:
        return 1

    # print([(n-1, k-1-i) for i in range(1, k)])
    # return sum([A(n-1, k-1-i) for i in range(1, k)])
    return sum([A(n-1, i) for i in range(k-2+1)])


for k in range(1, 12+1):
    b = ceil(k / 2)
    print(k, sum([A(n, k) for n in range(b+1)]))
