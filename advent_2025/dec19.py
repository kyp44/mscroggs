from __future__ import annotations
from common import *
from typing import List, Optional, Set
from dataclasses import dataclass


def union(sets) -> Numbers:
    return Numbers(*reduce(set.union, sets, set()))


def intersection(sets) -> Numbers:
    return Numbers(*reduce(set.intersection, sets, sets[0]))


class Numbers:
    def __init__(self, *args):
        self.ns = set(args)

    def __str__(self):
        return fr"\braces{{{', '.join([str(n) for n in sorted(self.ns)])}}}"

    def __iter__(self):
        for n in sorted(self.ns):
            yield n

    def digits_set(self) -> Numbers:
        return union([digits(n) for n in self.ns])

    def is_valid(self) -> bool:
        n = len(self.digits_set().ns)
        return n == 9 and len(list(it.chain.from_iterable(
            [digits(n) for n in self.ns]))) == n

    def with_num_digits(self, nd: int) -> Numbers:
        return Numbers(*filter(lambda n: len(digits(n)) == nd, self.ns))

    def filter_by_numbers_digits(self, nums: Numbers, num_digs=None) -> Numbers:
        if num_digs is None:
            num_digs = {1, 2, 3}
        bds = nums.digits_set()
        return Numbers(*filter(lambda n: len(bds.ns.intersection(digits(n))) == 0 and len(digits(n)) in num_digs, self.ns))

    def with_these(self, ns: Numbers, num_digs=None):
        print(f"With {self}: {ns.filter_by_numbers_digits(self, num_digs)}")

    @classmethod
    def squares(cls) -> Numbers:
        """
        All square numbers up to 1000 with no repeat digits
        """
        ns = []
        for k in range(1, 32):
            n = k**2
            ds = digits(n)
            if len(ds) == len(set(ds)):
                ns.append(n)
        return Numbers(*ns)


# Look at how many digits of numbers there can be
print("Possible combinations of n-digit numbers:")
combs = set()
for squares in it.product(range(1, 3+1), repeat=5):
    if sum(squares) == 9 and max(squares) == 3:
        combs.add(tuple(sorted(squares, reverse=True)))
combs = sorted(combs)
for comb in combs:
    print(comb)
print()

squares = Numbers.squares()

print("All squares of interest:")
print(squares)
print()
print(
    f"Possibilities for {combs[1]}:")
Numbers(1, 4, 9).with_these(squares, {3})
print()

Tns = {}
n12s = squares.filter_by_numbers_digits(Numbers(), num_digs={1, 2})
for n12 in n12s:
    Tn = squares.filter_by_numbers_digits(Numbers(n12), num_digs={3})
    print(
        fr"T_{{{n12}}} &= {Tn} \non")
    Tns[n12] = Tn
print()

print(f"Possibilities for {combs[0]}:")
for nd1s in it.combinations(squares.with_num_digits(1).ns, r=2):
    for nd2s in it.combinations(squares.filter_by_numbers_digits(Numbers(*nd1s), num_digs={2}).ns, r=2):
        ns = Numbers(*nd1s, *nd2s)
        nd3s = intersection([Tns[n].ns for n in ns])
        latex_row(
            f"${ns}$",
            f"${r' \cap '.join([f'T_{{{n}}}' for n in ns])} = {
                nd3s if len(nd3s.ns) > 0 else r'\es'}$",
        )
print()


for cs in it.combinations(squares.ns, r=5):
    cs = Numbers(*cs)
    if cs.is_valid():
        pans(max(cs.ns))
