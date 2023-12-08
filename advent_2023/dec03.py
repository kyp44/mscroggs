from common import *
from itertools import count

for i in count():
    n = 15*i

    if sum(digits(n)) == 15:
        pans(n)
        break
