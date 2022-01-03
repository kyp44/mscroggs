from pylab import *
from common import *

xs = linspace(-5, 5, 500)

g = lambda x : 8*x - 8 - x**2
h = lambda x : x**2
f = lambda x : 4*x-4

def makeplot(fname, showf) :
    figure()
    plot(xs, g(xs), label="$g$")
    plot(xs, h(xs), label="$h$")
    if showf :
        plot(xs, f(xs), label="$f$")

    grid()
    xlim(xs[0], xs[-1])
    xlabel("$x$")
    legend(loc="lower right")
    savefig(fname + ".png")

makeplot("dec10_gh", False)
makeplot("dec10_gfh", True)

print(g(-4))

pans(f(65))
