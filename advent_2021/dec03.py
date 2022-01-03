from common import *

s = 0
for n in range(1, 1000+1) :
    s += sum([1 for d in digits(n) if d == 0])
print("Brute force answer:", s)
pans(9 + 18 + 2*81 + 3)
