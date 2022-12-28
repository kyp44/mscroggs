from common import *


for n in range(100, 1000):
    # Digits
    ds = [int(d) for d in str(n)]

    # Check sum of digits
    if sum(ds) != 14:
        continue

    # Product of digits
    if product(ds) != 36:
        continue

    # Palindrome in base 9
    b9s = base(n, 9)
    if b9s != "".join(list(reversed(b9s))):
        continue

    pans(n)
