import itertools as it
from common import *

cnt = 0
for sides in it.combinations(range(1,15+1), 3) :
    sides = sorted(sides)

    if sides[0] + sides[1] > sides[2] :
        cnt += 1

pans(cnt)
