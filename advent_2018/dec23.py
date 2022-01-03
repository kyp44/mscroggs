from common import *
from pylab import *

p = 23

"""
ass = linspace(1, 22, 500)
As = ass*(p-ass)

plot(ass, As)
grid()
savefig("dec23.png")
"""
As = [a*(p-a) for a in range(1, 22+1)]
pans(max(As))
    
