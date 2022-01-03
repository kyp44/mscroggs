from common import *
from scipy.special import binom

# Number of sides of dimension k for hypercube with dimension n
def nums(n, k) :
    if n-k < 0 :
        return 0
    return 2**(n-k) * int(round(binom(n, n-k)))

def doit(lab, f) :
    print(lab)
    for n in range(7+1) :
        print(n, f(n))
    print()

doit("Points", lambda n : nums(n, 0))
doit("Squares", lambda n : nums(n, 2))
doit("n - 2", lambda n : nums(n,n-2))

pans(nums(8, 6))
