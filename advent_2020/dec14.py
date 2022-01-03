from common import *

cnt = 0
bcnt = 0
for n in range(10, 999+1) :
    ds = digits(n)
    if len(set(ds)) == len(ds) :
        cnt += 1
    else :
        bcnt += 1
pans(cnt)
