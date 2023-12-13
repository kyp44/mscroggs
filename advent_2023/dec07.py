from common import *


def In(n): return set(range(1, n+1))


def consecutive(s):
    """
    Whether a set contains consecutive integers.
    """
    for x in s:
        if x - 1 in s or x + 1 in s:
            return True

    return False


def Nn(n): return len([s for s in powerset(In(n)) if not consecutive(s)])


for n in range(14+1):
    print(n, "&", Nn(n), r"\\")

print()
pans(Nn(14))
