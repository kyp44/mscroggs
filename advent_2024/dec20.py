from pylab import *
from common import *

xs = linspace(-2, 10, 501)


def f(x): return x**2 - 2*x + 2
def g(x): return 4*x - 9
def p(x): return x**2 - 2*x + 1


def h(x): return x**2 - 6*x + 10


print(f"Minimum: ({3}, {h(3)})")

"""
plot(xs, 4*xs - 9)
plot(xs, xs**2 - 2*xs + 2)
plot(xs, xs**2 - 2*xs + 1)
show()
"""

pans(p(23))
