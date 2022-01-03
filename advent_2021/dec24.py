from common import *

def num(n) :
    """
    The number of n-digit numbers that
    contain two 2's and rthe rest 1's.
    """
    cnt = 0
    for n in range(10**(n-1), 10**n) :
        if product(digits(n)) == 20 :
            cnt += 1
    return cnt

numa = lambda n : n**2 * (n-1) // 2

for n in range(3, 7+1) :
    print(n, num(n), numa(n))

a = numa(12)
pans(a)
