from numpy import *
from common import *

# Converts digit array to integer
num = lambda arr : int("".join([str(d) for d in arr]))

# Numbers of digits
nds = {"1A" : 2,
       "3A" : 3,
       "7A" : 2,
       "1D" : 2,
       "2D" : 3,
       "4D" : 3,
       "6D" : 2}

fs = {"1A" : lambda n : n % 3 == 0,
      "3A" : lambda n : n > 300,
      "7A" : lambda n : n % 13 == 0,
      "1D" : lambda n : sqrt(n) == int(sqrt(n)),
      "2D" : lambda n : prod(digits(n,nds["2D"])) == 4,
      "4D" : lambda n : sum(digits(n)) == 11,
      "6D" : lambda n : n < 20}

# Initial possible values for each slot
pvals = dict([(k, list(range(10**nds[k]))) for k in fs.keys()])

# Filter everything based on all conditions
for k in fs.keys() :
    # Filter current slot
    pvals[k] = list(filter(fs[k], pvals[k]))

    # Filter based on other slots
    for ok in fs.keys() :
        if ok == k :
            continue

        pvals[k] = list(filter(lambda n : not fs[ok](n), pvals[k]))

# Returns possible numbers for each slot digit
def pdigits(k) :
    return [set([digits(n, nds[k])[dn] for n in pvals[k]]) for dn in range(nds[k])]

# Eliminates digits from values
def edigits(k, dn, edigs) :
    pvals[k] = list(filter(lambda n : digits(n, nds[k])[::-1][dn] not in edigs, pvals[k]))

# Show possible digits
for k in fs.keys() :
    print(k, pdigits(k))
