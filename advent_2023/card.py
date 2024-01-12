from copy import copy
from common import *
from common.probs import factorial_minus


prob(1)
pans(factorial_minus(1))

prob(2)
pans(factorial_minus(44))


def prob7_brute(d, k, n):
    valid_digs = set(range(1, d+1))
    cnt = 0
    for i in range(10**(n-1), 10**n):
        ds = digits(i)
        if set(ds).issubset(valid_digs):
            if len([x for x in ds if x == 1]) == (n-k):
                cnt += 1
    return cnt


prob(7)
d, k, n = (5, 1, 3)
print("Formula:", binom(n, k)*(d-1)**k)
pans(prob7_brute(d, k, n))

prob(8)
d, k, n = (5, 1, 75)
print("Verification:", binom(n, k)*(d-1)**k)
# Takes too long
# print("Brute force verification:", prob7_brute(d, k, n))
pans(300//4)

prob(9)
prob9_table = {
    0: 1,
    1: 7,
    2: 49,
    3: 43,
}
def prob9_ans(n): return prob9_table[n % 4]


for n in range(5):
    x = 7**n
    latex_row(n, x, x % 100)
pans(prob9_ans(3))


prob(10)
pans(prob9_ans(9876543210))
