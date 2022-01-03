from common import *

def times() :
    for h in range(24) :
        for m in range(60) :
            yield (h,m)

ts = []            
for h,m in times() :
    s = sum(digits(h)) + sum(digits(m))
    if s == 14 :
        ts.append("{:02}".format(h) + ":" + "{:02}".format(m))

pans(len(ts))
