from common import *

n = 14
def N(n): return int(np.ceil(n/2))


# Method 1, brute force (Slow for large n)
""" count = 0
for ns in range(n, 1-1, -1):
    for ks in it.product(range(1, N(n)+1), repeat=ns):
        xs = [2*k-1 for k in ks]

        if sum(xs) == n:
            print(xs)
            count += 1

print()
pans(count) """


# Method 2, recursive
def f(n):
    if n < 3:
        return 1

    return sum([f(n - 2*k + 1) for k in range(1, N(n)+1)])


for n in range(1, 20):
    print(f"f({n}) = {f(n)}")
print()
pans(f(14))
