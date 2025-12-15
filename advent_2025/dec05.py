from common import *


def frc_latex(f: frc):
    if f.denominator == 1:
        return str(f.numerator)
    else:
        return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"


# Two digit numbers divisible by 4
ms = [4*i for i in range(3, 25)]
ms = [m for m in ms if 0 not in digits(m)]
print("1. m ∈", ms)
ms = [m for m in ms if product(digits(m)) > 25]
print("2. m ∈", ms)
d2s = [frc(m) / 4 / (product(digits(m)) - 25) for m in ms]
print(f"3. d2 ∈ [{', '.join([frc_latex(d2) for d2 in d2s])}]")

for n in range(1, 1000000):
    if n == 4*product(digits(n)):
        pans(n)
