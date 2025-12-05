from common import *
from numpy import sqrt


def nf(S): return int(round((-1 + sqrt(1 + 8*sqrt(S))) / 2))
def Sbf(s): return int(round(s*(sqrt(1 + 8*s) - 1) / 2))


def doit(S):
    n = nf(S)
    print("n =", n)
    pans(Sbf(sqrt(S)))


print("Example:")
doit(36)

print("\nActual:")
doit(2025)
