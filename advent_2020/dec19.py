from common import *
from scipy.special import binom

N = lambda n : 2*(n+1)*int(binom(n+1, 2)) + n*(n+2) + 1

for n in (2, 7) :
    print("Number of cross lines on each side:", n)
    print("Number of tris with both lower verts:", 1 + n*(n+2))
    print("Number of tris with only one lower vert:", 2*(n+1)*int(binom(n+1, 2)))
    print("Total number of triangles:", N(n))
    print()

pans(N(n))
