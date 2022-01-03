from numpy import *
from common import *

# Blue square stuff
Ab = 14
sb = sqrt(Ab)
db = sb/sqrt(2)

# Red square from derived formula
Ar = 8*Ab
sr = sqrt(Ar)
dr = sr/sqrt(2)

# Small circle radius
r = sr / 2

# Big circle radius
R = dr + r

# Check big square diagonal
print(R + 2*db, sqrt(2)*R)

pans(8*Ab)
