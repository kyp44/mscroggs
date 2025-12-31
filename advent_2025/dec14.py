from __future__ import annotations
from common import *
from com import Seq


class Fib:
    def __init__(self, n: int):
        self.n = n
        self.F = Fib.calculate(n)

    def __str__(self):
        return f"F({self.n}) &= {self.F}"

    @classmethod
    def calculate(cls, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return Fib.calculate(n-1) + Fib.calculate(n-2)


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
    row.add(Fib(seq_len))
row.flush()

print()
pans(len(Seq.all_no_odd(11)))
