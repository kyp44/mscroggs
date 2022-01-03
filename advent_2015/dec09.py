from common import *

w = 7

s = 0
for a in range(w+1) :
    for b in range(a+1) :
        for c in range(b+1) :
            for d in range(c+1) :
                for e in range(d+1) :
                    s += 1

f = lambda w : (w**5 + 15*w**4 + 85*w**3 + 225*w**2 + 274*w + 120) / 120

print("Sum:", s)
print("Formula:", f(w))
pans(GridRoutes((w, 5)).routes())
