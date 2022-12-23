from common import *

bad_digs = {0, 1, 2, 3, 4}

nums = []
for n in range(100, 1000) :
    if len(bad_digs.intersection(set(digits(n)))) == 0 :
        nums.append(n)

print(nums)
pans(len(nums))