from common import *

N = 1000

closed = dict([(n+1, True) for n in range(N)])

def facts(n) :
    fs = []
    for k in range(1,n+1) :
        if n % k == 0 :
            fs.append(k)

    return fs

for n in range(1, N+1) :
    m = 1
    while m*n <= N :
        closed[m*n] = not closed[m*n]
        m += 1

# Verify factorization method
for n in range(1,N+1) :
    fs = facts(n)
    cl = len(fs) % 2 == 0
    if closed[n] != cl :
        print("BAD!")

pans(len([v for v in closed.values() if v]))
