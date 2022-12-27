from common import *
from pylab import *

maxn = int(ceil((999**2 - 4) / 17**2))
for n in range(1, maxn+1) :
    h = sqrt(n*17**2 + 4)

    if int(h) == h :
        print(n)
        pans(int(h))
        break
