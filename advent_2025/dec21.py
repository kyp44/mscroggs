from __future__ import annotations
from common import *
from com import Seq


class FibLike:
    def __init__(self, n: int):
        self.n = n
        self.F = FibLike.calculate(n)

    def __str__(self):
        return f"T({self.n}) &= {self.F}"

    @classmethod
    def calculate(cls, n):
        def T(n):
            if n == 1:
                return 2
            else:
                return S(n) + T(n-1)

        def S(n):
            if n == 1:
                return 1
            elif n == 2:
                return 1
            else:
                return T(n-2) + S(n-2)

        return T(n)


class Row:
    def __init__(self):
        self.row = []

    def full(self) -> bool:
        return len(self.row) == 4

    def add(self, f: FibLike):
        self.row.append(f)
        if self.full():
            self.flush()
            self.row = []

    def flush(self):
        print(" & ".join([str(x) for x in self.row]),
              r"\non" if self.full() else "")


print(f"Example: {len(Seq.all_no_even(4))}\n")

row = Row()
for seq_len in range(1, 11+1):
    row.add(FibLike(seq_len))
row.flush()
print()

pans(len(Seq.all_no_even(11)))
