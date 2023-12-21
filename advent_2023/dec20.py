from common import *
from math import comb
import itertools as it


def all_combos(s, max_n):
    """
    Generates all combinations pulled from the set
    `s` from one up to `max_n` elements.
    """
    for n in range(1, max_n+1):
        for combo in it.combinations(s, n):
            yield combo


def box_combos(k, n):
    def boxes(k, s):
        if k == 1:
            return [[s]]

        n = len(s)
        if n < k:
            raise ValueError("There must be at least as many balls as boxes")

        bxs = []
        for curr_box in all_combos(s, n - k + 1):
            cb = set(curr_box)
            for others in boxes(k - 1, s - cb):
                bxs.append([cb] + others)

        return bxs

    return boxes(k, set(range(1, n+1)))


k, n = 4, 5

cnt = 0
for boxes in box_combos(k, n):
    print(boxes)
    cnt += 1


def N(k, n):
    if k == 1:
        return 1

    return sum([binom(n, i) * N(k-1, n - i) for i in range(1, n-k+1+1)])


print("Recursion verification:", N(k, n))
pans(cnt)
