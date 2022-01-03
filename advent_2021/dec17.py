from common import *

for n in it.count() :
    if product(digits(n)) == 252 :
        pans(n)
        break
