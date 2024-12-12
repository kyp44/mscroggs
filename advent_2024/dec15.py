from common import *

ps = []

for n in range(1, 9+1):
    a = n**2
    b = number(digits(a)[::-1])
    p = a*b

    latex_row(n, a, b, p, "Yes" if len(digits(p)) == 3 else "No")

    if a % 10 != 0:
        ps.append(p)

print()
pans(min(ps))
