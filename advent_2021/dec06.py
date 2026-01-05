from common import *

c1 = 12345
r1 = 205
c2 = 6789
r2 = 112

d = c1 - c2
print("c difference:", d)
f = d - r1 + r2
print("factor of:", f)
fs = factors(f)
print("factors:", fs)

# Get answer
for x in fs:
    if len(digits(x)) == 3:
        break

# Verify original congruence


def cong(c):
    print(c, "mod", x, "=", c % x)


cong(c1)
cong(c2)

pans(x)
