from common import *
f = lambda n : (n**2 + n + 2) / 2

for n in range(10+1) :
    print(n, f(n))

pans(f(17))
