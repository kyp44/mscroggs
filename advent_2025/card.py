from __future__ import annotations
from common import *
import math
prob(1)


def S(N):
    return sum([n for n in range(N+1) if n % 2 == 1])


def Sa(N):
    return N**2//4


N = 12
print("Analytical:", Sa(N))
pans(S(N))

prob(2)
N = 44444
print("Analytical:", Sa(N))
pans(S(N))

prob(3)


def system_mod_1_brute(*args) -> int:
    for x in it.count(2):
        if set([x % m for m in args]) == {1, }:
            return x
    return -1


pans(system_mod_1_brute(3, 4))

prob(4)
pans(system_mod_1_brute(*range(2, 9+1)))

prob(5)
pans(123)

prob(6)
pans(sum([factorial(9) // factorial(9 - nd) for nd in range(1, 9+1)]))

prob(7)


class Diophantine:
    def __init__(self, a: int, b: int):
        """
        Linear diophantine equations ax + by.
        """
        self.a = a
        self.b = b
        self.d = gcd(a, b)

        # Find base solution for a*x0 + b*y0 = d
        (self.x0, self.y0) = np.array(EEA.new(a, b).run())

    def print_info(self):
        print(f"(x_0, y_0) = ({dio.x0}, {dio.y0})")
        print("c_max =", dio.max_bad_c())

    def max_bad_c(self) -> int:
        """
        Returns c_max where
        ax + by = c 
        Always has at least one positive integer solution for c > x_max.
        """
        c_max = frc(self.a*self.b, self.d)
        assert c_max.is_integer()
        return int(c_max)

    def may_have_solution(self, c: int) -> bool:
        """
        Returns whether the equations
        ax + by = c
        may have positive integer solutions.
        """
        return c % self.d == 0

    def t_bounds(self, c: int) -> Optional[Tuple[frc, frc]]:
        """
        Return the bounds for the multiple solution parametrized by t
        or None if there are no solutions.
        """
        if not self.may_have_solution(c):
            return None

        return (frc(-c*self.x0, self.b), frc(c*self.y0, self.a))

    def solve(self, c: int) -> Optional[Tuple[int, int]]:
        """
        Finds a positive integer solution for ax + by = c.
        """
        # Verify that a solution is possible without even determining bounds.
        bds = self.t_bounds(c)
        if bds is None:
            return None

        # Bounds for a positive solution for ax + by = n
        (l, u) = bds
        # cl = math.ceil(l)
        # t = cl if l <= cl else cl + 1
        fu = math.floor(u)
        t = fu if fu <= u else fu - 1
        if l <= t <= u:
            x = frc(c*self.x0 + self.b*t, self.d)
            y = frc(c*self.y0 - self.a*t, self.d)
            assert x.is_integer() and y.is_integer()
            return (int(x), int(y))

        return None

    def largest_no_solution(self) -> Optional[int]:
        """
        Through brute force, calculates the largest c with no solution for
        ax + by = c
        Returns None if there infinitely many such c.
        """
        if self.d > 1:
            return None

        for c in range(self.max_bad_c(), 0, -1):
            if self.solve(c) is None:
                return c
        return None


dio = Diophantine(4, 5)
dio.print_info()
pans(dio.largest_no_solution())

prob(8)
dio = Diophantine(495371, 2921695)
dio.print_info()
pans(dio.largest_no_solution())

prob(9)


def smallest_no_sum(nd: int) -> Optional[int]:
    for x in range(10**(nd-1), 10**nd):
        for n in factors(2*x)[1:]:
            m = frc(2*x + n*(1 - n),  2*n)
            if m.is_integer() and m > 0:
                break
        else:
            return x
    return None


pans(smallest_no_sum(2))

prob(10)
for x in range(10**3, 10**4):
    if x % 4 == 2:
        assert x % 2 == 0 and x // 2 % 2 == 1
        pans(x)
        break

prob(11)


def num_lines(np: int) -> int:
    return np*(np-1) // 2


pans(num_lines(18))

prob(12)
for n in quadratic_rational(1, -1, -166047976*2):
    if n > 0:
        pans(n)
