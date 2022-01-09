from common import *

A = set(range(1,7+1))

def f(n, R) :
    if len(R) == 0 :
        return 1
    Bn = {k for k in R if k > n or k in factors(n)}
    if len(Bn) == 0 :
        return 0
    return sum([f(k, R - {k}) for k in Bn])

pans(sum([f(n, A - {n}) for n in A]))
