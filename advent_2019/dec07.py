from scipy.special import binom
from common import *

n = 5

# Example binomial
print("Example:", sum([binom(n,k) for k in range(n+1)]))

# From Wolfram Alpha
print("Alpha:", sum([32, 80, 80, 40, 10, 1]))

# From analysis
pans(sum([binom(n,k)*2**k for k in range(n+1)]))
