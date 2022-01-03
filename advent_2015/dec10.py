from common import *

mis = [2, 3, 5, 7, 11, 13]
M = product(mis)
xis = [(-i) % mi for i,mi in enumerate(mis)]
Mis = [M // mi for mi in mis]
his = [[n for n in range(mi) if (Mi*n) % mi == 1][0] for Mi, mi in zip(Mis, mis)]


print("xis =", xis)
print("Mis =", Mis)
print("his =", his)

print("x =", sum([xi*Mi*hi for xi, Mi, hi in zip(xis, Mis, his)]) % M, "(mod", str(M) + ")")

x = 788

def try_mod(a, p) :
    if (x + a) % p != 0 :
        print("x +", a, "is not divisible by", p)

try_mod(0, 2)
try_mod(1, 3)
try_mod(2, 5)
try_mod(3, 7)
try_mod(4, 11)
try_mod(5, 13)

pans(x)
