from common import *
import pylab as pl

xs = pl.linspace(-4, 8, 500)
f1 = lambda x : x**2 + 4*x + 14
f2 = lambda x : 2*x**2 + 8*x + 18

print(f1(-2), f2(-2))

f = lambda x : 3./2*x**2 + 6*x + 16
print(f(-2), f(2))

pl.plot(xs, f1(xs))
pl.plot(xs, f2(xs))
pl.plot(xs, f(xs))
pl.grid()
pl.savefig("plot.png")

pans(f(6))
