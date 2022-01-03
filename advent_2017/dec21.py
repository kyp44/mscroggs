from common import *

def fact(n) :
    fs = []
    for k in range(1, n // 2 + 1) :
        if n % k == 0 :
            fs.append(k)

    return fs

for n in range(100, 999+1) :
    if sum(fact(n)) == n :
        pans(n)
