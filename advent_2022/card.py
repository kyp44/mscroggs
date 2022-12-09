from common import *


def prob(n):
    sep = "".join(["-" for i in range(20)])
    print(sep + " Problem " + str(n) + " " + sep)


prob(6)
digital_sums(7, num_digs=4, analytical=lambda s: (s**3 - 6*s**2 + 11*s - 6)/6)

prob(7)
digital_sums(7)
