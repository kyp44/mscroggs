from common import *
N = 1000

cnt = 0

for n in range(1,N+1) :
    s = str(n)
    cnt += len([d for d in s if d == "1"])

pans(cnt)
