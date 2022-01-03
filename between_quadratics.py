from pylab import *

f = lambda x : x**2 - 2*x + 2
fp = lambda x : 2*x - 2
g = lambda x : 2*x**2 - 4*x + 3
gp = lambda x : 4*x - 4


xs = linspace(-10, 20, 500)

plot(xs, f(xs))
plot(xs, g(xs))
plot(16, f(16), "o")
plot(16, g(16), "o")
grid()
savefig("plot.png")

figure()
plot(xs, fp(xs))
plot(xs, gp(xs))
grid()
savefig("pplot.png")

M = array([[1, 1, 1], [121, 11, 1], [2, 1, 0]])
b = array([1, 181, 0])
coeff = linalg.solve(M, b)

print polyval(coeff, 16)
