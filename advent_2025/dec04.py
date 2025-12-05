from common import *
from numpy import average

a = 24
N = 225

print("Analytical:", 2*(N + 2*a + 2))

sums = []
for a in range(1000):
    n = sum(range(a, a+4))
    if len(digits(n)) == 3:
        sums.append(n)

pans(int(round(average(sums))))
