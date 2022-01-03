from common import *

# Integer/long factorial function
def fact(n) :
    if n == 0 :
        return 1

    return n*fact(n-1)

# Calculate required factorial
fs = str(fact(611))

# Count the number of zeros at the end
c = 1
while fs[-c] == "0" :
    c += 1

pans(c-1)
