import numpy as np
from math import factorial
from math import gcd
from common import *

def prob(n) :
    sep = "".join(["-" for i in range(20)])
    print(sep + " Problem " + str(n) + " " + sep)
    
    return True

def pans(a) :
    print("Answer:", a)

if prob(1) :
    N = 10000
    cnt = 0
    for n in range(1,N+1) :
        s = str(n)
        cnt += len([d for d in s if d == "1"])

    pans(cnt)

if prob(2) :
    a = sum([n for n in range(86) if n % 2 == 1])
    pans(a)

if prob(3) :
    def factors(n) :
        if n == 1 :
            return set((1,))
        fs = set()
        for k in range(1,n//2+1) :
            if n % k == 0 :
                fs.add(k)
                fs.add(n // k)

        return fs

    N = 4008004

    ns = []

    """
    # Brute force method (very slow)
    for n in range(1, N+1) :
        if len(factors(n)) % 2 == 1 :
            ns.append(n)
    """

    # Insightful shortcut
    ns = [k**2 for k in range(1, int(np.ceil(np.sqrt(N)))+1) if k**2 <= N]

    #print(ns)
    pans(len(ns))

if prob(4) :
    N = 130404

    pans(N+1)

if prob(5) :
    rs = 60153
    pans(2*rs)

if prob(6) :
    def f(n) :
        if n < 1 :
            raise ValueError("invalid parameter: " + str(n))
        if n == 1 :
            return 1
        elif n == 2 :
            return 2
        else :
            return f(n-1) + f(n-2)

    pans(f(28))

if prob(7) :
    def lcm(a, b) :
        return a*b // gcd(a,b)
    pans(lcm(1025, 835))

if prob(8) :
    # Number reversed as a string
    istr = str(factorial(245))[::-1]

    # Count the leading zeros
    cnt = 0
    for c in istr :
        if c == "0" :
            cnt += 1
        else :
            break

    pans(cnt)

if prob(9) :
    for n in range(10**5, 10**6) :
        for dd in range(6+1) :
            ds = digits(n)
            if dd > len(ds)-1 :
                continue
            ds.pop(dd)
            nd = number(ds)
            if n + nd == 334877 :
                pans(n)
