from common import *
N = 1000

def fact(n) :
    return (1 if n == 0 else n*fact(n-1))

def tz(s) :
    c = 0
    for k in range(1,1000+1) :
        if s[-k] == "0" :
            c += 1
        else :
            break
    return c

try :
    s = str(fact(N))
    print("Zeros after " + str(N) + "!")
    print(tz(s))
except :
    print("Recursion too deep to calculate " + str(N) + "!")

for e in range(1, 1000+1) :
    b = 10**e
    
    # Calculate the factorial mod b
    p = 1
    for k in range(2, N+1) :
        p = (p * k) % b
        if p == 0 :
            break
    else :
        print("Should be " + str(e-1) + " zeroes")
        break
