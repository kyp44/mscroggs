from common import *

k = 50

# Brute force answer
cnt = 0
for c in range(k-1, 0, -1) :
    for b in range(c, 0, -1) :
        for a in range(b, 0, -1) :
            if a + b + c == 2*k :
                cnt += 1
pans(cnt)
