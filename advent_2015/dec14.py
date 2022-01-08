from common import *

for n in range(100, 1000) :
    # Check that n is prime
    if len(factors(n)) > 2 :
        continue

    # Check that n is a palindrome
    if tuple(digits(n)) != tuple(reversed(digits(n))) :
        continue

    # Check that n in binary is a palindrome
    bs = bin(n)[2:]
    if bs != bs[::-1] :
        continue

    # n is our answer!
    pans(n)
    break
