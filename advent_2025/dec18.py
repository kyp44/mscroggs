from __future__ import annotations
from common import *
from typing import List, Optional
from dataclasses import dataclass


def valid_sets(n: int):
    for s in powerset(range(1, n+1)):
        if len(s) == 0:
            continue
        if len(s) == min(s):
            yield sorted(s)


def show_sets(n: int):
    print(f"Sets for {n} elements:")
    ss = list(valid_sets(n))
    for s in ss:
        print(s)
    print("Number of sets:", len(ss))
    print()


def num_valid_sets(N: int) -> int:
    return len(list(valid_sets(N)))


def S(N, n):
    return binom(N-n, n-1)


def T(N):
    sum([S(N, n+1) for n in range(N)])


def F(n: int) -> int:
    if n in (0, 1):
        return 1

    return F(n-2) + F(n-1)


print("Example:")
show_sets(5)

N = 14
print("Analytical:", T(N))
print("Fibonacci", F(N-1))
pans(len(list(valid_sets(N))))
