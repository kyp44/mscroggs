from common import *
from math import factorial

for n in it.count() :
    if count_ending_zeros(factorial(n)) == 50 :
        pans(n)
        break
