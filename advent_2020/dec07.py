from common import *

N = lambda a, b : check_div((b+1)*(b - 2*a + 2) + a*(a-1), 2)
#S = lambda a, b : check_div(sum([(2*b + 3)*i - 3*i**2 + b*(b+1) for i in range(a,b+1)]), 2)
#S = lambda a, b : check_div((2*b + 3)*check_div(b*(b+1) - a*(a-1), 2) - check_div(b*(b+1)*(2*b+1) - a*(a-1)*(2*a-1), 2) + b*(b+1)*(b-a+1), 2)
S = lambda a, b : check_div((b - a + 2)*(b*(b+1) - a*(a-1)), 2)

def sol(lab, a, b) :
    print(lab + ":")
    print("Number of dominoes:", N(a, b))
    print("Sum analytical:", S(a, b))
    print("Sum manual:", sum([i + j for i in range(a,b+1) for j in range(i,b+1)]))
    print()
    return S(a,b)

sol("Example", 0, 4)
pans(sol("Problem", 5, 10))
