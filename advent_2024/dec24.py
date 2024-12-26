from common import *

good_digits = {1, 2, 3, 4, 5, 6, 7}

ns = [n for n in range(100, 1000) if len(set(digits(n)) - good_digits) == 0]

pans(np.mean(ns))
