import itertools as it
from common import *

prob(1)


def Nodd(n):
    s = 0
    for x in range(n+1):
        if x % 2 == 1:
            s += x
    return s


pans(Nodd(30))

prob(2)
pans(Nodd(5668))

prob(3)


def digits_sum_prod(s, p):
    for n in it.count():
        digs = digits(n)

        if sum(digs) == s and product(digs) == p:
            return n


pans(digits_sum_prod(28, 10000))

prob(4)
pans(digits_sum_prod(41, 432000))

prob(11)


def count_diff_digits(n):
    cnt = 0
    for nd in range(1, n+1):
        for p in it.permutations(range(1, 9+1), nd):
            cnt += 1
    return cnt


pans(count_diff_digits(2))

prob(12)
pans(count_diff_digits(9))

prob(13)
for n in it.count(1):
    fs = factors(n)
    if product(fs) == 2**len(fs):
        pans(n)
        break

prob(14)
for n in it.count(1):
    fs = factors(n)
    if product(fs) == 25**len(fs):
        pans(n)
        break
