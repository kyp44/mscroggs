from __future__ import annotations
from typing import List
from common import it


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

    def has_even_ones(self) -> bool:
        num_ones = 0

        for n in self.seq:
            if n == 0:
                if num_ones > 0 and num_ones % 2 == 0:
                    return True
                num_ones = 0
            else:
                num_ones += 1
        return num_ones > 0 and num_ones % 2 == 0

    @classmethod
    def all(cls, n: int) -> List[Seq]:
        return [Seq(*s) for s in it.product((0, 1), repeat=n)]

    @classmethod
    def all_no_odd(cls, n: int) -> List[Seq]:
        return [s for s in cls.all(n) if not s.has_odd_ones()]

    @classmethod
    def all_no_even(cls, n: int) -> List[Seq]:
        return [s for s in cls.all(n) if not s.has_even_ones()]


class Row:
    def __init__(self):
        self.row = []

    def full(self) -> bool:
        return len(self.row) == 4

    def add(self, x):
        self.row.append(x)
        if self.full():
            self.flush()
            self.row = []

    def flush(self):
        print(" & ".join([str(x) for x in self.row]),
              r"\non" if self.full() else "")
