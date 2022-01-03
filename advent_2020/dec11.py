import numpy as np
from common import *

m = 108

ra = m
rb = 0
ba = check_div(m, 2)
bb = check_div(rb + m, 2)

print("ra:", ra)
print("ba:", ba)
print("rb:", rb)
print("bb:", bb)

print("Pile A % red before move:", ra / (ra + ba))
print("Pile B % red after move:", (rb + m) / (rb + m + bb))
pans(ra + rb + ba + bb)
