from common import *


def an(n): return n*(n-2) + 2
def bn(n): return (n+1)*(n-1) + 1


x = None
for n in range(1, 20+1):
    a = an(n)
    b = bn(n)
    latex_row(n, a, b)
    if a <= 300 <= b:
        x = b
pans(x)
