from pylab import *

xs = linspace(-3, 3, 500)

plot(xs, xs**4 - 4*xs**3)
grid()
savefig("f.png")
clf()

plot(xs, 4*xs**3 - 12*xs**2)
grid()
savefig("fp.png")
