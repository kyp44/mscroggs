from common import *
from math import factorial as fact

def checkp(p) :
    for i in range(len(p) - 1) :
        if p[i+1] == p[i] + 1 :
            return False
    else :
        return True

def Nb(n) :
    cnt = 0
    for p in it.permutations(range(1,n+1)) :
        if checkp(p) :
            cnt += 1
            #print(p)
    return cnt

def Nr(n) :
    if n in (1, 2) :
        return 1
    else :
        return (n-1)*Nr(n-1) + (n-2)*Nr(n-2)

print("Example:", Nb(3), Nr(3))
print("Acutal problem:", Nb(6), Nr(6))
pans(Nb(6))
