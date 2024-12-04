"""
Tried to solve the logic puzzle using a brute force program because
solving it via logical deduction seemed to require a lot of
guesswork.

This failed due to the clues being self-referential. As such, this program
doesn't actual work, but I'm leaving it for reference.
"""
from common import *
from dataclasses import dataclass
from typing import Callable, Iterable, Optional


clues = {
    1: lambda s, ct: s["C"] in [1, 8, 0],
    2: lambda s, ct: s["C"] in [6, 8, 1],
    3: lambda s, ct: s["A"] == 5,
    4: lambda s, ct: s["C"] in [6, 8, 1],
    5: lambda s, ct: s["D"] in [3, 7, 8],
    6: lambda s, ct: s["E"] in [2, 3],
    7: lambda s, ct: s["D"] in [9, 8, 7],
    8: lambda s, ct: len([x for x in s.values() if x == 2]) == 2,
    9: lambda s, ct: all([ct[cn] == False for cn in factors(600) if cn < 25]),
    10: lambda s, ct: s["C"] == 5,
    11: lambda s, ct: s["E"] != 0,
    12: lambda s, ct: len([x for x in s.values() if x % 2 == 0]) == 2,
    13: lambda s, ct: s["E"] != 8+1,
    14: lambda s, ct: s["C"] not in [3, 9],
    15: lambda s, ct: s["C"] == 4,
    16: lambda s, ct: s["A"] == 2 and s["B"] == 1,
    17: lambda s, ct: s["A"] == 2 and s["B"] == 2,
    18: lambda s, ct: len([x for x in s.values() if x == 1]) >= 1,
    19: lambda s, ct: s["E"] not in [4, 5],
    20: lambda s, ct: len([x for x in s.values() if x % 2 == 0]) == 4,
    21: lambda s, ct: s["C"] != 2,
    22: lambda s, ct: s["E"] != 7,
    23: lambda s, ct: False,
    24: lambda s, ct: len([cv for cv in ct.values() if cv == True]) < 10,
    # 24: lambda s, ct: False,
}

for sv in it.product(range(10), repeat=5):
    sockets = {k: v for k, v in zip("ABCDE", sv)}

    ct = {k: None for k in clues.keys()}
    last_ct = None

    # This loop is because a clue truth value will often flip back and forth
    # for ever if the number of iterations is not limited
    for i in range(20):
        ct = {k: clues[k](sockets, ct)
              for k in clues.keys()}

        # print(ct)
        if ct == last_ct:
            break
        last_ct = ct
    else:
        continue

    if ct[9] == True:
        print(sockets)
        # print(ct)
