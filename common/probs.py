# These are solutions to particular problem, but multiple problems
from common import *
from math import factorial as fact


def digital_sums(s, num_digs=None, analytical=None):
    """
    Counts the number of numbers with nonzero digits whose digital sum is
    s, with either a specific number of digits (num_digs) or among all natural
    numbers (num_digs = None). An optional analytical solution function f(s)
    may be passed to ensure that this matches the other methods.

    See the Advent 2022, Dec 6 problem for details.
    """
    def N(m, s):
        """
        Recursive function
        """
        if m == 1:
            return 1
        else:
            return sum([N(m-1, j) for j in range(m-1, s-1+1)])

    sol = sum([N(m, s) for m in range(1, s+1)]
              ) if num_digs is None else N(num_digs, s)
    print("Recursive solution:", sol)

    if analytical is not None:
        print("Analytical solution:", analytical(s))

    # Direct, brute force solution
    nums = []
    if num_digs is None:
        for n in range(number([1 for i in range(s)]) + 1):
            ds = digits(n)
            if 0 not in ds and sum(ds) == s:
                nums.append(n)
    else:
        for n in range(10**(num_digs-1), 10**num_digs):
            ds = digits(n)
            if 0 not in ds and sum(ds) == s:
                nums.append(n)

    pans(len(nums))


def factorial_minus(a):
    """
    Searches for the largest n such that (n! - a)
    is a multiple of (n - a).

    See, for example, the Advent 2023, Dec 4 problem.
    """
    ans = -1

    for n in range(1, 1000):
        x = fact(n) - a
        y = n - a

        if y != 0 and x % y == 0:
            ans = n

    return ans
