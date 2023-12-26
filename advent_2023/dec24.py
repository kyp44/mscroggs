from common import *


def double_zeros(bds):
    for i in range(len(bds)-1):
        if bds[i] == 0 and bds[i+1] == 0:
            return True

    return False


for n in range(100, 1000):
    bds = digits(str(bin(n))[2:])[::-1]

    if bds[-1] == 1 and not double_zeros(bds):
        print("Binary:", bds)
        pans(n)
        break
