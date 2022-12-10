import numpy as np
import matplotlib.pyplot as plt
from common import *

b = -160000

a = np.sqrt(-4*b)

pans(a)


def f(x): return x**2 - a*x


D = 100
xm = a/2
xs = np.linspace(xm-D, xm+D, 500)

fig, ax = plt.subplots()

ax.plot(xs, f(xs))
ax.axhline(b)
fig.savefig("dec10.png")
