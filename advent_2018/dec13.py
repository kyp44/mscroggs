from common import *

N = 1000

# Closed and locked sets
all = frozenset(range(1,N+1))
locked = set((1,))
closed = set((1,))

# Simulation
while len(closed) < N :
    #print("Locked:", locked)
    #print("Closed:", closed)

    # Close and lock the first open locker
    n = min(all - closed)
    locked.add(n)
    closed.add(n)

    # Now toggle all multiple of locked locker number
    m = 2
    while m*n <= N :
        k = m*n
        if k in locked :
            raise ValueError("Somehow a locker got locked that should not have!")
        if k in closed :
            closed.remove(k)
        else :
            closed.add(k)
        m += 1

pans(len(locked))
