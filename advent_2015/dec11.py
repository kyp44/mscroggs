from common import *

for d2 in range(10) :
    f = 97*d2 - 1
    latex_row(d2, f, f % 299, f % 20)

print()
for d0 in range(1, 4) :
    print(d0, 299*d0)

print()
for d2 in range(10) :
    f = 97*d2 - 300
    latex_row(d2, f)
    
print()
for d2 in range(10) :
    f = 97*d2 - 599
    latex_row(d2, f)
    
x = 742
print()
print("Verified:", x == 3*number(reversed(digits(x))) + 1)
pans(x)
