from common import *

xs = [729, 313, 328]

a = sum(xs) / 2

print("Sum:", sum(xs))
print("Verification:", 4/3*np.mean(xs + [a]))
pans(a)
