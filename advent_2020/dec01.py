from math import factorial as fact
from common import *

# Number of digits to choose
digits = (1, 2, 3, 4, 5)
N = len(digits)

print("Analytical:")
# Number of numbers in the example
nT = sum([check_div(fact(N), fact(N-nd)) for nd in range(1, N+1)])
print("Total:", nT)

# Number of even and odd digits
Ne = 2
No = N - Ne

# Number of even numbers
ne = sum([check_div(No*fact(N-1), fact(N-nd)) for nd in range(1, N+1)])
pans(ne)

# Brute force approach
print()
print("Brute force:")
(nT, ne) = (0, 0)
for nd in range(1, N+1) :
    for ds in it.permutations(digits, nd) :
        n = number(ds)
        nT += 1
        if n % 2 == 1 :
            ne += 1
print("Total:", nT)
pans(ne)
