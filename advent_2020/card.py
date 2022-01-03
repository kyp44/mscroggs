import numpy as np
from math import factorial as fact
from math import gcd
from scipy.special import binom
from common import *

def prob(n) :
    sep = "".join(["-" for i in range(20)])
    print(sep + " Problem " + str(n) + " " + sep)

prob(1)
N = 6
no = sum([4*fact(N-1) // fact(N - nd) for nd in range(1, N+1)])
print("Analytical:", no)
no = 0
digits = (1, 2, 3, 4, 5, 7)
for nd in range(1, N+1) :
    for ds in it.permutations(digits, nd) :
        n = number(ds)
        if n % 2 == 1 :
            no += 1
pans(no)

prob(2)
Ns = 40300
N = 4*Ns
pns = lambda n : (2*n-1, 2*n, N + 2*(1-n) - 1, N + 2*(1-n))
print("Analytical:", 2*(N+1))
ss = [sum(pns(n)) for n in range(1, Ns+1)]
pans(max(ss))

prob(3)
Nm = 130376
N = Nm // 2
print("Analytical:", N**2)
pans(sum([n for n in range(Nm+1) if n % 2 == 1]))

prob(4)
b = np.array([31, 35, 36])
A = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
Ar = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
for Arc in it.permutations(Ar) :
    A = np.array(Arc)
    x = np.linalg.solve(A, b)
    print("Sum of cards:", sum(x))
pans(int(sum(b)) // 2)

prob(5)
Vp = 1337
pans(3*Vp)

prob(6)
a, b = 305, 671
print("gcd:", gcd(a, b))
pans(a*b // gcd(a, b))

prob(7)
Ns = 6
b = np.array([6136, 9999])
A = np.array([[1, 1], [6, -1]])
n, i = [int(v) for v in np.linalg.solve(A, b)]
print(n, i)
pans(n)
"""
s = 6
# Calculates the number of combinations of n dice with sum p
# From: https://www.lucamoroni.it/the-dice-roll-sum-problem/
def Ns(n, p) :
    kmax = int(np.floor((p -n) / s))
    return int(sum([(-1)**k * binom(n, k) * binom(p - s*k - 1, p - s*k - n) for k in range(kmax + 1)]))

n = 2
print()
ss = [sum(dv) for dv in it.product(range(1, s+1), repeat=n)]
for i in range(5*n+1) :
    p = n + i
    Nsb = len([s for s in ss if s == p])
    print(p, Nsb, Ns(n, p))
"""

prob(8)
Nk = lambda k, n, m : (n - k + 1)*(m - k + 1) if n >= k and m >= k else 0
n, m = 14, 16
p = min(n, m)
print("Analytical:", p*n*m + (p*(p-1)*(2*p - 3*n - 3*m - 1)) // 6)
pans(sum([Nk(k, n, m) for k in range(1,p+1)]))

prob(9)
s = 155667
for d0 in range(10) :
    N = 10*s + d0
    if N % 11 == 0 :
        print(d0)
        pans(N // 11)
