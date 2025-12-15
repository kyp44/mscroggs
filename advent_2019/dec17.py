from common import *


def d1(d2, d0): return frc(584 - 101*(d2 + d0), 20)


for d2, d0 in ((1, 3), (6, 8), (5, 9)):
    print(d2, d0, d1(d2, d0))


def test(x):
    # Check number of digits
    if len(digits(x)) != 3:
        return False

    # Get reversed number
    digs = digits(x, 3)
    y = sum([d*10**i for i, d in enumerate(digs[::-1])])

    # Check comparison
    if not (y > x):
        return False

    # Check sum
    if x + y != 584:
        return False

    # All tests passed
    return True


# Check analytical solution
sol = 193
print("Solution:", sol)
print("Verified:", test(sol))

# Brute force check every three-digit number
print("Brute force solutions:")
for x in range(100, 1000):
    if test(x):
        print(x)


pans(sol)
