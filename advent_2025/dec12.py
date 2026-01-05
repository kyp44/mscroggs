from __future__ import annotations
from common import *


@dataclass
class Numbers:
    a: int
    b: int
    c: int

    def sum(self) -> int:
        return self.a + self.b + self.c

    def max(self) -> int:
        return max(self.as_set())

    def as_set(self) -> set:
        return set([self.a, self.b, self.c])

    def __str__(self):
        return f"a = {self.a}, b = {self.b}, c = {self.c}"

    def __eq__(self, other):
        return self.as_set() == other.as_set()

    def __hash__(self) -> int:
        return hash(frozenset(self.as_set()))


ns = []
for all_digits in it.permutations(range(1, 7+1)):
    n = Numbers(
        number(all_digits[:3]),
        number(all_digits[3:6]),
        all_digits[6]
    )

    if n.sum() == 1000:
        ns.append(n)

min_n = min(ns, key=lambda n: n.max())
min_ns = set(filter(lambda n: n.max() == min_n.max(), ns))
for n in min_ns:
    print(n)

pans(min_n.max())
