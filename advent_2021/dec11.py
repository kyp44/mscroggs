from common import *

def fr(n) :
    if n == 1 :
        return 1
    else :
        return fr(n-1) + 2*n - 3

f = lambda n : n*(n-2)+2
    
for n in range(1, 30+1) :
    print(n, fr(n), f(n))

a = 750
n = 28
pans(a - 2*(n-1))

