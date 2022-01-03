from common import *

for n in range(100,999+1) :
    ns = str(n)
    if ns == ns[::-1] and "0" not in ns :
        #print(n)
        for ds in ns :
            d = int(ds)
            if n % d == 0 :
                break
        else :
            pans(n)
            break
    
