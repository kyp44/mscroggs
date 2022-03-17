from common import *
from collections import Counter
dbg = False

tabs = lambda lvl : "".join(["\t" for i in range(lvl)])

def sums(n, used=None, lvl=0) :
    if dbg :
        print(tabs(lvl) + "Entered sums:", n, used)

    if n == 0 or (used and n in used) or n % 9 == 0:
        return []
    elif n == 1 :
        return [[1]]

    ss = [[n]]
    nused = (used if used else []) + [n]
    for k in range(1, n) :
        if k in nused or k % 9 == 0 :
            continue
        lss = sums(n - k, nused + [k], lvl+1)
        for ls in lss :
            if dbg :
                print(tabs(lvl) + "Appending:", [k] + ls)
            ss.append([k] + ls)

    # Remove duplicates.
    # This is annoying but there is no better way
    # because Counters are mutable and therefore
    # not hashable, so they cannot be put into sets
    css = [Counter(s) for s in ss]
    ss = [s for i,s in enumerate(ss) if Counter(s) not in css[i+1:]]

    if dbg :
        print(tabs(lvl) + "Returning from sums:", ss)

    return ss
        
res = sums(35)
for v in res :
    print(v)
pans(len(res))
