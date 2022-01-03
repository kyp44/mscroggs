from common import *

sol = np.array([[2, 5, 2],
                [2, 1, 6],
                [2, 2, 1]])

across = lambda r : number(sol[r-1,:][::-1])
down = lambda c : number(sol[:,c-1][::-1])

def check(c) :
    if not c :
        print("Verication failed")
        exit(0)

palindrome = lambda n : digits(n) == digits(n)[::-1]
cubes = [n**3 for n in range(1, 10+1) if len(digits(n**3)) == 3]

check(not (palindrome(across(1)) ^ palindrome(down(1))))
check(not (across(1) > 350 or down(1) < 150))
check(not (down(3) % 2 == 1 and across(2) == down(2)))
check((len(factors(down(3))) == 2) ^ (across(3) % 2 == 1))
check(across(2) in cubes and down(2) in cubes)
check(sum(digits(down(3))) == 2 or sum(digits(across(3))) == 5)

print("Verification passed")
pans(down(1))
