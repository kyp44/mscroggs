from common import *

w = 7

s = 0
for a in range(w+1) :
    for b in range(a+1) :
        for c in range(b+1) :
            s += 1
f = lambda w : (w**3 + 6*w**2 + 11*w + 6) / 6

print("Sum:", s)
print("Formula:", f(w))
pans(GridRoutes((w, 3)).routes())
