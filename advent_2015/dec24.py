from common import *

anss = [
    200,
    154,
    304,
    108,
    208,
    385,
    138,
    240,
    792,
    788,
    742,
    252,
    729,
    313,
    328,
    685,
    205,
    834,
    147,
    280,
    720,
    128,
    587,
]

r = 0
for n in anss :
    for k in anss :
        if k >= n :
            continue
        rl = n % k
        if rl > r :
            #print(n, k)
            r = rl
pans(r)
