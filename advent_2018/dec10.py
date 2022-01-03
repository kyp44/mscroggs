from common import *
from pylab import *
import numpy as np

c = 414720

def facts(n) :
    fs = []
    for k in range(1,n+1) :
        if n % k == 0 :
            fs.append(k)

    return fs

fs = np.array(facts(c))
N = len(fs)

"""
# Lists all the unique values of b

print("Positive solutions:")
for n in fs[0:N//2] :
    m = c // n
    b = -(m + n)
    print("b =", b, "n =", n, "m =", m, "f(n) =", n**2 + b*n + c, "f(m) =", m**2 + b*m + c)

print("Negative solutions:")
for n in -fs[0:N//2] :
    m = c // n
    b = -(m + n)
    print("b =", b, "n =", n, "m =", m, "f(n) =", n**2 + b*n + c, "f(m) =", m**2 + b*m + c)
"""

pans(N)
exit()

# Brute force approach that searches for values of b

print("Generating squares set...")
sqs = dict(((n**2, n) for n in range(int(1e7)+1)))
maxsq = max(sqs.keys())

b = int(ceil(sqrt(4*c)))
cnt = 0
while True :
    d = b**2 - 4*c
    if d > maxsq :
        break

    if d in sqs :
        x1 = (-b + sqs[d]) / 2
        x2 = (-b - sqs[d]) / 2
        x3 = (b + sqs[d]) / 2
        x4 = (b - sqs[d]) / 2
        print(b, x1, x2, x3, x4)
        print("Div", c % x1, c % x2, c % x3, c % x4)
        cnt += 2
        #print("b / count:", b, cnt)

    b += 1

print("Answer:", cnt)
