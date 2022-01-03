from pylab import *
import itertools as it
from math import gcd

wait = False

def lcm(a,b):
    return abs(a * b) / gcd(a,b) if a and b else 0

def facts(n) :
    fs = []
    for k in range(1, n // 2 + 1) :
        if n % k == 0 :
            fs.append(k)
    fs.append(n)
    return fs

def fint(x) :
    return int(round(x))

def prob(pn, ans) :
    #print("Problem", pn, "answer:", ans)
    print("Problem", pn, "answer:", fint(ans))

# Problem 1    
n = 1000
while True :
    ds = [int(d) for d in str(n)]
    if sum(ds) == 6 :
        prob(1, n)
        break
    n += 1

# Problem 2
a = 152560
b = 114420
prob(2, sqrt(a**2 + b**2))

# Problem 3
prob(3, lcm(1346, 196))

# Problem 4
# This formula was derived as part of a 2018 advent calendar problem
n = 696 // 2
prob(4, (n+1)**2)

# Problem 5
# Similar to problem in 2018 advent calendar problem
"""
c = 0
for n in range(100,10000+1) :
    for d in [int(ds) for ds in str(n)] :
        if d in (0,1,2,3) :
            break
    else :
        c += 1
print(c)
"""
prob(5, 6**4 + 6**3)

# Problem 6
prob(6, 14*20*10*40)

# Problem 7
N = 16020308
p = N // 2
prob(7, 2*p + 1)

# Problem 8
if wait :
    s = 18745225
    for n in range(s//2, s+1) :
        ns = str(n)
        m = int(ns[:-1])
        if n + m == s :
            break
    prob(8, n)

# Problem 9
m = 13
n = 119
prob(9, (m-1)*n - m)

# Problem 10
(n, m) = (7, 6)
c = 0
for seq in it.product((0,1), repeat=(n+m)) :
    if sum(seq) == m :
        #print(seq)
        c += 1
prob(10, c)
