import itertools as it
import numpy as np
from common import *

sol = (6, 11, 13)
print("Solution:", sol)

cards = list(range(2,14+1))

print("Brute force solutions:")
for table in it.combinations(cards, 3) :
    left = set(cards) - set(table)
    for hand1 in it.combinations(left, 5) :
        hand2 = tuple(sorted(left - set(hand1)))
        if np.product(hand1) == np.product(hand2) :
            print(table, hand1, hand2)

pans(np.product(sol))
