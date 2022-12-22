from common import *

n = 35
print(n)
while True :
    next = number(digits(n)[::-1]) + 6
    print(next)
    if next < n :
        n = next
        break
    n = next

pans(n)
