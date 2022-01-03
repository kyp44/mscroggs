from common import *
import itertools as it
import numpy as np

N = 13

L = np.array((-1, 0))
R = np.array((1, 0))
U = np.array((0, -1))
D = np.array((0, 1))

ps = set()

#for k,s in enumerate(it.product((L, R, U, D), repeat=N)) :
for k,s in enumerate(it.combinations_with_replacement((L, R, U, D), N)) :
    print("Sequence", k+1)
    ps.add(tuple(sum(s)))

print(ps)
pans(len(ps))
