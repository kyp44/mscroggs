from common import *

def rev(n) :
    return int(str(n)[::-1])

for n in range(100, 999+1) :
    if n + 2 == rev(2*n) :
        pans(n)
