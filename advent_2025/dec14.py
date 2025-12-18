from __future__ import annotations
from common import *
from typing import List
from dataclasses import dataclass


class Seq:
    vals = ["B", "A"]

    def __init__(self, *args):
        # Verify
        seq = list(args)
        for n in seq:
            assert n in (0, 1), "sequence must contain only 0 or 1"
        self.seq = seq

    def __str__(self):
        return "".join([self.vals[i] for i in self.seq])

    def has_odd_ones(self) -> bool:
        num_ones = 0

        for n in self.seq:
            if n == 0:
                if num_ones % 2 == 1:
                    return True
                num_ones = 0
            else:
                num_ones += 1
        return num_ones % 2 == 1

    @classmethod
    def all(cls, n: int) -> List[Seq]:
        return [Seq(*s) for s in it.product((0, 1), repeat=n)]

    @classmethod
    def all_valid(cls, n: int) -> List[Seq]:
        return [s for s in cls.all(n) if not s.has_odd_ones()]


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


@dataclass
class Fib:
    n: int
    F: int

    def __str__(self):
        return f"F({self.n}) &= {self.F}"


class Row:
    def __init__(self):
        self.row = []

    def full(self) -> bool:
        return len(self.row) == 4

    def add(self, f: Fib):
        self.row.append(f)
        if self.full():
            self.flush()
            self.row = []

    def flush(self):
        print(" & ".join([str(x) for x in self.row]),
              r"\non" if self.full() else "")


row = Row()
for seq_len in range(1, 11+1):
    row.add(Fib(seq_len, fib(seq_len)))
row.flush()

print()
pans(len(Seq.all_valid(11)))
