import operator as op
import numpy as np
from collections import namedtuple
import itertools as it
import argparse
import os
from functools import reduce
from fractions import Fraction as frc
from math import factorial, gcd, comb as binom
from enum import Enum, auto
import roman
from tqdm import tqdm
from multiset import Multiset
from sympy import factorint


def powerset(iterable):
    """
    The power set of an iterable
    """
    s = set(iterable)
    return list(set(x) for x in it.chain.from_iterable(it.combinations(s, r) for r in range(len(s)+1)))


def check_div(a, b):
    """
    Integer division where a ValueError is
    thrown if the numbers are not divisible.
    """
    if a % b != 0:
        raise ValueError("a not evenly divisible by b")

    return a // b


def digits(n, nd=None):
    """
    Converts an integer to a list of its digits.
    Can optionally specify number of digits
    to pad with zeros.

    The digits are returned in order from least
    significant to most.
    """
    ds = str(n) if nd is None else ("{:0" + str(nd) + "}").format(n)
    return [int(d) for d in ds][::-1]


def number(ds):
    """
    Converts a digit array into an integer number.

    The digits are assumed to be in order from least
    significant to most.
    """
    return sum([d*10**e for (e, d) in enumerate(ds)])


def power_number(n, p):
    """
    Returns whether is another number to a certain power.
    """
    for k in it.count():
        m = k**p
        if m == n:
            return True
        elif m > n:
            return False


def square_number(n): return power_number(n, 2)
def cubic_number(n): return power_number(n, 3)


class GenGrid:
    """
    Represents and can solve a general 3x3
    grid puzzle.
    """

    def __init__(self, rowchecks, colchecks, genchecks=[], digits=True):
        """
        The first three argument should be an iterable of three
        functions, that checks the corresponding rows
        and columns. Each of these functions should
        take a 3-element iterable for the row/col
        and should return a boolean, i.e. whether or not
        the row/col condition is satisfied.

        The `digits` argument is whether or not each digit must
        be used exactly once in the grid (True) or whether
        duplicate digits are allows (False).
        """
        self.rowchecks = rowchecks
        self.colchecks = colchecks
        self.genchecks = genchecks
        self.digits = digits

    def check(self, sol):
        # Verify that solution uses each digit exactly once
        if self.digits:
            if len(set(sol.flatten())) != 9 or np.min(sol) != 1 or np.max(sol) != 9:
                return False

        # Check each row
        for row, check in zip(sol, self.rowchecks):
            if not check(row):
                return False

        # Check each column
        for col, check in zip(sol.T, self.colchecks):
            if not check(col):
                return False

        # General checks (the grid as a whole)
        for check in self.genchecks:
            if not check(sol):
                return False

        return True

    def brute(self):
        if self.digits:
            numss = it.permutations(range(1, 9+1), 9)
            numss_size = factorial(9)
        else:
            numss = it.product(range(9+1), repeat=9)
            numss_size = 10**9

        # Try every possible grid configuration.
        # Tried to do this in parallel with a thread pool, but this is extremely broken
        # in Python on Linux.
        sols = []
        for nums in tqdm(numss, total=numss_size, leave=False):
            sol = np.array(nums).reshape(3, 3)
            if self.check(sol):
                sols.append(sol)

        return sols


def check_grid(args):
    """
    Returns the solution or None if it fails the check.
    """
    gen_grid, nums = args


class EquGrid(GenGrid):
    """
    Represents and can solve an equation digit
    grid puzzle.
    """
    Equ = namedtuple("Equ", ("first", "sec", "equ"))

    # Operators
    class Oper(Enum):
        ADD = auto()
        SUB = auto()
        MUL = auto()
        DIV = auto()

    def __init__(self, fname):
        opers = {
            "+": self.Oper.ADD,
            "-": self.Oper.SUB,
            "*": self.Oper.MUL,
            "/": self.Oper.DIV,
        }

        # Read lines from file
        with open(fname, "r") as f:
            lines = [l.strip() for l in f]

        # Parse rows and columns
        self.highlighted = []
        self.rows = []
        self.cols = []
        for rc in range(3):
            sp = lines[2*rc].split()
            self.rows.append(self.Equ(opers[sp[1]], opers[sp[3]], frc(sp[-1])))
            self.cols.append(self.Equ(opers[lines[1].split()[rc]], opers[lines[3].split()[
                             rc]], frc(lines[-1].split()[rc])))

            # Highlighted cells
            for n in [n for n, v in enumerate(sp) if v == "^"]:
                self.highlighted.append((rc, n // 2))

        # Create the check functions for the general grid
        def checkf(checkequ, sol):
            opers = {
                self.Oper.ADD: op.add,
                self.Oper.SUB: op.sub,
                self.Oper.MUL: op.mul,
                self.Oper.DIV: op.truediv,
            }

            if opers[checkequ.sec](opers[checkequ.first](sol[0], sol[1]), sol[2]) != checkequ.equ:
                return False
            return True

        super().__init__([lambda sol, r=r: checkf(self.rows[r], sol) for r in range(
            3)], [lambda sol, c=c: checkf(self.cols[c], sol) for c in range(3)])

    def highlighted_sol(self, sol):
        """
        Returns list of highlighted cells in a solution.
        They are ordered from left to right and top to
        bottom.
        """
        return [sol[c] for c in self.highlighted]

    def print_latex(self):
        """
        Prints LaTeX code for this grid in terms of the
        grid box macros.
        """
        opers = {
            self.Oper.ADD: "+",
            self.Oper.SUB: "-",
            self.Oper.MUL: r"\times",
            self.Oper.DIV: r"\div",
        }
        gsym = r"\gridsym"
        gblank = r"\gridblank"

        for rn, row in enumerate(self.rows):
            rg = 6 - 2*rn

            # Number cells
            for cn in range(3):
                boxh = "h" if (rn, cn) in self.highlighted else ""
                print(r"\gridbox" + boxh + latex_args(2 *
                      cn, rg, "#" + str(3*rn + cn + 1)))

            # Operators and result
            print(gsym + latex_args(1, rg, opers[row.first]))
            print(gsym + latex_args(3, rg, opers[row.sec]))
            print(gsym + latex_args(5, rg, "="))
            print(gsym + latex_args(6, rg, row.equ))

        # Column operators and result
        for cn, col in enumerate(self.cols):
            print(gsym + latex_args(2*cn, 5, opers[col.first]))
            print(gsym + latex_args(2*cn, 3, opers[col.sec]))
            print(gsym + latex_args(2*cn, 1, "="))
            print(gsym + latex_args(2*cn, 0, col.equ))

        # Blanks
        print(gblank + latex_args(1, 5))
        print(gblank + latex_args(3, 5))
        print(gblank + latex_args(1, 3))
        print(gblank + latex_args(3, 3))


class GridRoutes:
    """
    Represents a grid, possibly with removed nodes, and
    calculates the number of routes from the lower left node
    to the upper right moving in a set of directions, without
    revisiting any nodes.
    """
    class Direction(Enum):
        UP = auto()
        DOWN = auto()
        LEFT = auto()
        RIGHT = auto()

    def __init__(self, size, directions=(Direction.UP, Direction.RIGHT), removed=[]):
        """
        Takes the size of the grid as a tuple (w, h), and an
        optional list of tuples (x, y) of removed nodes, relative
        to the lower left corner being (0, 0) and the upper right
        being (w, h).
        """
        self.size = size
        self.directions = directions
        self.removed = removed

    def routes(self, node=(0, 0), visited=None):
        """
        Calculates recursively the number of routes from the
        lower left corner to the upper right (or vice versa).
        """
        if visited is None:
            visited = set(self.removed)

        # Removed nodes are not allowed
        (x, y) = node
        if node in visited or x < 0 or x > self.size[0] or y < 0 or y > self.size[1]:
            return 0
        # End node
        if node == self.size:
            return 1

        # Recurse
        s = 0
        visited.add(node)

        def try_dir(direction, dx, dy):
            if direction in self.directions:
                return self.routes((x + dx, y + dy), visited.copy())
            return 0
        s += try_dir(self.Direction.UP, 0, 1)
        s += try_dir(self.Direction.DOWN, 0, -1)
        s += try_dir(self.Direction.LEFT, -1, 0)
        s += try_dir(self.Direction.RIGHT, 1, 0)
        return s


def factors(n):
    """
    Find factors of a number.
    """
    if n == 0:
        return set()
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
# Print answer


def pans(a):
    print("Answer:", a)


def product(ns):
    """
    Product (the numpy version doesn't work so well)
    """
    p = 1
    for n in ns:
        p *= n
    return p


def base(n, b):
    """
    Change b to a base-n number.
    Up to base-36 is supported without special notation.
    """
    num_rep = {10: 'a',
               11: 'b',
               12: 'c',
               13: 'd',
               14: 'e',
               15: 'f',
               16: 'g',
               17: 'h',
               18: 'i',
               19: 'j',
               20: 'k',
               21: 'l',
               22: 'm',
               23: 'n',
               24: 'o',
               25: 'p',
               26: 'q',
               27: 'r',
               28: 's',
               29: 't',
               30: 'u',
               31: 'v',
               32: 'w',
               33: 'x',
               34: 'y',
               35: 'z'}

    st = ""
    cur = n
    while cur != 0:
        rem = cur % b
        if 36 > rem > 9:
            st = num_rep[rem]
        elif rem >= 36:
            remst = '(' + str(rem) + ')'
        else:
            remst = str(rem)
        st = remst + st
        cur = int(cur / b)
    return st


def box_solutions(year, day, sol, ansf, brute):
    """
    Verifies solution to a box sum puzzle and
    optionally shows uniqueness by finding
    all solutions by brute force. Also generates
    LaTeX code for the puzzle and solution with
    a command line option
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Verifies and solves the box puzzle and generates LaTeX code for it.")
    parser.add_argument("--code", "-c", action="store_true",
                        help="Generate LaTeX code instead of solving.")
    args = parser.parse_args()

    # Read in grid
    grid = EquGrid("dec{:02}-grid.txt".format(day))

    if args.code:
        tag = "@advent@" + \
            roman.toRoman(year - 2000).lower() + "@" + \
            roman.toRoman(day).lower()
        print(r"\newcommand\grid" + tag + "[9]{")
        print(r"\begin{center}")
        print(r"\begin{tikzpicture}")
        grid.print_latex()
        print(r"\end{tikzpicture}")
        print(r"\end{center}")
        print("}")
        print(r"\def\gridsol" + tag +
              r"{\grid" + tag + latex_args(*sol.flatten()) + "}")
    else:
        # Read in expression grid and check solution
        print("Solution:")
        print(sol)
        print("Solution verified:", grid.check(sol))

        if brute:
            print("Brute force solutions:")
            sols = grid.brute()
            for s in sols:
                print(s)

            pans(ansf(grid.highlighted_sol(sol)))


def anumber(a): return number(a[::-1])


def box_gen_solutions(rowchecks, colchecks, sol, ansf, brute, genchecks=[], digits=True):
    print("Solution:")
    print(sol)
    grid = GenGrid(rowchecks, colchecks, genchecks, digits)
    print("Solution code:", "".join(
        ["{" + str(v) + "}" for v in sol.flatten()]))
    print("Solution verified:", grid.check(sol))

    if brute:
        print("Brute force solutions:")
        sols = grid.brute()
        for s in sols:
            print(s)

            pans(ansf(sol))


# These functions are useful in an interactive session to solve general box puzzles
def adigits(a):
    """
    For a list of 3-digit numbers, returns three sets of each digit.
    """
    return [set([digits(n)[::-1][dn]
                 for n in a]) for dn in range(3)]


def three_digits(a):
    """
    Filters an iterable of numbers to keep only
    those with three digits.
    """
    return [n for n in a if len(digits(n)) == 3]


def remove_duplicate_digits(a):
    """
    Removes numbers from an iterable that have duplicate
    digits.
    """
    return [n for n in a if len(digits(n)) == len(set(digits(n)))]


def remove_digit(a, d):
    """
    Removes all numbers that contain a digit at all.
    """
    return [n for n in a if d not in digits(n)]


def filter_digits(a, d1=None, d2=None, d3=None):
    """
    Filters an array of 3 digit nubmers, where digits
    match optionally passed sets for each digit.

    a - Iterable of 3 digit numbers
    d1 - Set of acceptable first (most significant) digits (None for no filtering)
    d2 - Set of acceptable second (middle) digits (None for no filtering)
    d3 - Set of acceptable third (least significant) digits (None for` no filtering)
    """
    for dn, ds in enumerate((d1, d2, d3)):
        if ds is not None:
            a = [n for n in a if digits(n)[::-1][dn] in ds]
    return a


def cross_filter(a1, dn1, a2, dn2):
    """
    Filter to arrays of 3-digit numbers based on certain digits
    in each being the same.

    a1 - First array of numbers
    dn1 - Digit number in first array numbers to filter (0-2 MSD first)
    a2 - Second array of numbers
    dn2 - Digit number in second array numbers to filter (0-2 MSD first)

    Return (a1, a2) filtered.
    """
    ds = adigits(a1)[dn1].intersection(adigits(a2)[dn2])
    return (
        [n for n in a1 if digits(n)[::-1][dn1] in ds],
        [n for n in a2 if digits(n)[::-1][dn2] in ds],
    )


def latex_args(*args):
    """
    Returns args converted to strings with each in braces
    for a list of LaTeX arguments.
    """
    return "".join(["{" + str(v) + "}" for v in args])


def latex_row(*args):
    """
    Prints a row of a LaTeX tabular with the given values,
    which will be converted to strings.
    """
    print(" & ".join([str(v) for v in args]), r"\\")


def count_ending_zeros(n):
    # Number reversed as a string
    istr = str(n)[::-1]

    # Count the leading zeros
    cnt = 0
    for c in istr:
        if c == "0":
            cnt += 1
        else:
            break
    return cnt


def all_primes(limit=None):
    """
    Generator that produces all primes of at most the limit, or without bound if limit is `None`.
    """
    yield 2
    primes_so_far = [2]
    n = 3
    while True:
        if limit is not None and n > limit:
            break
        is_prime = True
        for p in primes_so_far:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes_so_far.append(n)
            yield n
        n += 2


class NotDivisibleError(Exception):
    pass


class PrimeFactors:
    """
    Class that represents a positive integer as a multiset of its
    unique prime factorization. Operations on these use these
    multisets instead of the integers themselves. This is useful
    for working with extremely large integers where actual integer
    operations would be slow and cumbersome.
    """

    def __init__(self, arg):
        if type(arg) is int:
            self.multiset = Multiset(factorint(arg))
        elif type(arg) is Multiset:
            self.multiset = arg
        elif type(arg) is PrimeFactors:
            self.multiset = arg.multiset
        else:
            raise TypeError()

    def __int__(self):
        return product(list(self.multiset))

    def __mul__(self, other):
        return PrimeFactors(self.multiset + PrimeFactors(other).multiset)

    __rmul__ = __mul__

    def ismultiple(self, other):
        """
        Whether this is a multiple of another number.
        """
        return self.multiset.issuperset(PrimeFactors(other).multiset)

    def isdivisor(self, other):
        """
        Whether this is a divisor of another number.
        """
        other.multiple(self)

    def __truediv__(self, other):
        if self.ismultiple(other):
            return PrimeFactors(self.multiset - PrimeFactors(other).multiset)
        else:
            raise NotDivisibleError

    def __pow__(self, other):
        return PrimeFactors(int(other) * self.multiset)

    def is_square(self):
        """
        Whether this is a square number.
        """
        # Verify that every exponent is even
        for x in set(self.multiset):
            if self.multiset[x] % 2 == 1:
                return False

        return True

    def is_perfect_power(self) -> bool:
        return gcd(*self.multiset.multiplicities()) > 1

    def factorial(self):
        p = 1
        for k in range(2, int(self)+1):
            p *= PrimeFactors(k)

        return p

    def __repr__(self):
        return repr(self.multiset)


def multinom(*params):
    """
    Multinomial coefficient:
    https://en.wikipedia.org/wiki/Multinomial_theorem
    """
    return product(binom(sum(params[:i]), x) for i, x in enumerate(params, 1))


def prob(n):
    """
    Prints a problem header, used in the Christmas card
    scripts.
    """
    sep = "".join(["-" for i in range(20)])
    print(sep + " Problem " + str(n) + " " + sep)
