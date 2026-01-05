from __future__ import annotations
from common import *
from typing import Optional


class Seq:
    def __init__(self, *args):
        # Verify
        seq = list(args)
        for n in seq:
            assert n in (0, 1), "sequence must contain only 0 or 1"
        self.seq = seq

    def __str__(self):
        return "".join([str(k) for k in self.seq])

    def len(self):
        return len(self.seq)

    def next(self) -> Optional[Seq]:
        if self.len() == 1:
            return None
        ns = []
        for (a, b) in zip(self.seq, self.seq[1:]):
            if a == b:
                ns.append(1)
            else:
                ns.append(0)
        return Seq(*ns)

    def reduction_iter(self):
        s = self
        while s is not None:
            yield s
            s = s.next()

    def fully_reduce(self) -> int:
        # Annoying that this is the best way to get the last item
        s = None
        for s in self.reduction_iter():
            pass
        return s.seq[0]

    @classmethod
    def all(cls, n: int):
        for s in it.product((0, 1), repeat=n):
            yield Seq(*s)


print("Example:")
seq = Seq(1, 1, 1, 0, 1)
for s in seq.reduction_iter():
    print(s)


print()
pans(len([s for s in Seq.all(10) if s.fully_reduce() == 1]))
