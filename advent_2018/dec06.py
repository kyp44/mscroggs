from common import *

def facts(n) :
    fs = []
    for k in range(1,n+1) :
        if n % k == 0 :
            fs.append(k)

    return fs

s = 0
for n in range(12,22+1) :
    fs = facts(n)
    lof = max([f for f in fs if f % 2 == 1])
    print(n, fs, lof)

    s += lof

pans(s)
