from common import *


def hf(n): return int(np.ceil(n/3))
def vf(n): return n - int(np.floor((n-2) / 3))


def all_colorings(num_cells, num_colored):
    return ([1 if k in xs else 0 for k in range(num_cells)] for xs in it.combinations(range(num_cells), num_colored))


def num_friendly_colored(bs, k): return len([j for j in filter(lambda j: j >= 0 and j <
                                                               len(bs), [k+i for i in range(-1, 1+1)]) if bs[j] > 0])


def all_have_friendly_colored(bs, required_colored):
    return all(num_friendly_colored(bs, k) >= required_colored for k in range(len(bs)))


def coloring_is_possible(num_cells, num_colored, required_colored):
    return any(all_have_friendly_colored(bs, required_colored) for bs in all_colorings(num_cells, num_colored))


def minimum_colored_num_required(num_cells, required_colored):
    for nc in it.count(1):
        if coloring_is_possible(num_cells, nc, required_colored):
            return nc


def check(label, af, bf):
    print(f"{label}:")
    for k in range(1, 10+1):
        n = 2*k + 1

        print(n, af(n), bf(n))
    print()


check("Horizontal", hf, lambda n: minimum_colored_num_required(n, 1))
check("Vertical", vf, lambda n: minimum_colored_num_required(n, 2))

n = 23
a = minimum_colored_num_required(n, 1) * minimum_colored_num_required(n, 2)
print("Total:", n, hf(n)*vf(n), a)
print()
pans(a)
