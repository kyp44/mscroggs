from common import *
from math import factorial as fact
from functools import reduce
import operator

def prod(l):
    return reduce(operator.mul, l, 1)

x = prod([fact(n) for n in range(1,216+1)])
nf = fact(108)
ks = x // nf

T1 = prod([(2*n+1)**(108-n) for n in range(0,108)])
T2 = 2**5832
T3 = prod([(n+1)**(107-n) for n in range(0,107)])

k = T1*T2*T3
print(ks - k**2)
