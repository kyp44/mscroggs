from common import *
from itertools import islice
import collections


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n-1), maxlen=n)
    for x in it:
        window.append(x)
        yield tuple(window)


first = None

for n in range(100, 1000):
    fs = sorted(factors(n))
    print(n, fs)
    fs = fs[1:-1]

    # Build sets of consecutive factors
    runs = []
    curr = set()
    for i, fc in enumerate(fs[:-1]):
        fn = fs[i+1]

        if fn == fc + 1:
            curr.add(fc)
            curr.add(fn)
        else:
            if len(curr) > 0:
                runs.append(sorted(curr))
            curr = set()

    # Go through each run
    for run in runs:
        # Go through window lengths
        for ln in range(2, len(run) + 1):
            for win in sliding_window(run, ln):
                if product(win) == n:
                    print(n, "=", win)
                    if first is None:
                        first = n

    if first is not None:
        break

pans(first)
