from common import *
from numpy import *
import itertools as it

dth = 2*pi / 26

pts = [array((cos(n*dth), sin(n*dth))) for n in range(26)]

def is_zero(x) :
    return abs(x) < 1e-10

c = 0
for p1,p2,p3 in it.combinations(pts, 3) :
    s1 = p2 - p1
    s2 = p3 - p2
    s3 = p1 - p3

    dp1 = dot(s1, s2)
    dp2 = dot(s2, s3)
    dp3 = dot(s1, s3)

    if is_zero(dp1) or is_zero(dp2) or is_zero(dp3) :
        c += 1

pans(c)
