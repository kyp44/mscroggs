from common import *

xs = np.array([-6, 17])
ys = xs**2

f = lambda x : (x - xs[0])*(ys[1] - ys[0])/(xs[1] - xs[0]) + ys[0]

print("f(xs):", f(xs), ys)
y0 = -xs[0]*xs[1]
print("f(0):", y0)

pans(y0)
