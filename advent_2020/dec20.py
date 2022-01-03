from common import *

def find(Nis) :
    for n in it.count() :
        sums = [None for n in Nis]

        for k in range(1, n) :
            for Ni,N in enumerate(Nis) :
                nss = [k + i for i in range(N)]
                if sum(nss) == n :
                    sums[Ni] = nss
        if len([s for s in sums if s is None]) == 0 :
            print("Sums:")
            for ss in sums :
                print(" + ".join(map(str, ss)), "=", n)
            return n

print("Example problem:")
find((3, 4))
print()
n = find((12, 13))
pans(n)
