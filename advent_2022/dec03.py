import numpy as np
import itertools as it
from common import *

M = np.array(range(1, 81+1)).reshape((9, 9))

print("All sums:", set([sum([M[n, pn] for n, pn in enumerate(pns)])
      for pns in it.permutations(range(9))]))
