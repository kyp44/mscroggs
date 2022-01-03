from common import *

ns = []
for n in range(100, 1000) :
    ds = digits(n)
    cs = sum([d**3 for d in ds])
    if n == cs :
        ns.append(n)

print("Qualifying numbers:", ns)
for n in ns :
    if n - 1 in ns :
        pans(n)
