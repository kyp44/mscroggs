from common import *

for n in it.count(2) :
    if len(factors(n)) == 2 :
        k = n
        for i in range(10) :
            k = 3*k + 16
            if len(factors(k)) > 2 :
                break
        else :
            pans(n)
            break
