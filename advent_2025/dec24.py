from __future__ import annotations
from common import *
from com import Row


@dataclass
class Pows:
    a: int
    b: int

    def value(self) -> int:
        return 3**self.a * 5**self.b

    def __str__(self):
        return f"3^{{{self.a}}} 5^{{{self.b}}} &= {self.value()}"


rows = Row()
for (a, b) in it.product(range(1, 6+1), range(1, 4+1)):
    rows.add(Pows(a, b))
rows.flush()

ns = [n for n in range(100, 1000) if PrimeFactors(n).primes() == {3, 5}]
pans(max(ns))
