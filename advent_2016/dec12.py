from common import *

def base(n, b):
    """\
    Change a  to a base-n number.
    Up to base-36 is supported without special notation.
    """
    num_rep={10:'a',
         11:'b',
         12:'c',
         13:'d',
         14:'e',
         15:'f',
         16:'g',
         17:'h',
         18:'i',
         19:'j',
         20:'k',
         21:'l',
         22:'m',
         23:'n',
         24:'o',
         25:'p',
         26:'q',
         27:'r',
         28:'s',
         29:'t',
         30:'u',
         31:'v',
         32:'w',
         33:'x',
         34:'y',
         35:'z'}

    st = ""
    cur = n
    while cur != 0 :
        rem = cur % b
        if 36 > rem > 9 :
            st = num_rep[rem]
        elif rem >= 36 :
            remst = '(' + str(rem) + ')'
        else:
            remst = str(rem)
        st = remst + st
        cur = int(cur / b)
    return st

for n in range(100, 1000) :
    # Digits
    ds = [int(d) for d in str(n)]

    # Check sum of digits
    if sum(ds) != 14 :
        continue

    # Product of digits
    if product(ds) != 36 :
        continue

    # Palindrome in base 9
    b9s = base(n, 9)
    if b9s != "".join(list(reversed(b9s))) :
        continue

    pans(n)
