from common import *


def do_it(one_valid: bool) -> int:
    for n in it.count(100):
        fs = sorted(factors(n))
        ofs = list(filter(lambda f: f % 2 == 1, fs))
        if not one_valid and len(ofs) == 1:
            continue
        if len(ofs) in ofs:
            return n
    return -1


pans(do_it(True))
