from common import *
from scipy.special import binom
import itertools as it

n = 4
k = 2

print(sum([binom(n, i) for i in range(1, n)]))


balls = set(range(1, n+1))


def all_combos(s, max_n):
    for n in range(1, max_n+1):
        for combo in it.combinations(s, n):
            yield combo


len([combo for combo in all_combos(balls, 3)])
