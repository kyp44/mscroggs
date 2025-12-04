from common import *

diff_nums = []
for n in range(100, 1000):
    if len(set(digits(n))) == 3:
        diff_nums.append(n)

pans(len(diff_nums))
