from common import *

N = 101

def ways(n) :
    bs = [3, 5, 7]
    mx = int(np.ceil(n / 3))

    cnt = 0
    for cs in it.product(range(mx+1), repeat=3) :
        k = np.dot(cs, bs)
        if k == n :
            cnt += 1
    return cnt

a = None
cleft = 0
for n in it.count() :
    w = ways(n)
    print(n, w)
    if w == N :
        a = n
    elif w > N :
        cleft += 1
        if cleft >= 3 :
            pans(a)
            break
    else :
        cleft = 0
