from common import *

letters = {"A" : 8,
           "E" : 6,
           "G" : 2,
           "H" : 9,
           "M" : 1,
           "R" : 3,
           "S" : 7,
           "T" : 4,
           "U" : 0,
           "X" : 5}

s2n = lambda s : number([letters[c] for c in s[::-1]])

# Check the sums
good = True

if s2n("XMAS") + s2n("MATHS") != s2n("GREAT") :
    good = False
if s2n("XMAS") + s2n("MATH") != s2n("SURE") :
    good = False

print("Sums checkout?", good)
pans(s2n("SAM"))
