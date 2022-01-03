from common import *
n = 107

dton = lambda ds : int("".join([str(d) for d in ds]))
    

while True :
    ds = [int(d) for d in str(n)]

    x = dton(sorted(ds))
    y = dton(sorted(ds, reverse=True))
    print(n)
    m = abs(x - y)
    if m == n :
        break
    n = m
