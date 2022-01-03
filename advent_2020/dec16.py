from common import *

sol = np.array([[3, 3, 3],
                [3, 3, 3],
                [3, 3, 3]])

nf = lambda ds : number(ds[::-1])
# Perform checks
good = True

# A1
if good :
    good = (nf(sol[0,:]) - 3) % 110 == 0

# A5
if good :
    good = (nf(sol[2,:]) - 30) % 101 == 0

# D1
if good :
    good = nf(sol[:,0]) == 37 * sum(sol[0,:])

# D2
if good :
    v = nf(sol[:,1])
    for f in factors(nf(sol[2,:])) :
        if v == 3*f :
            break
    else :
        good = False

# D3
if good :
    good = (nf(sol[:,2]) + 3) % 112 == 0
    
print("Valid solution:", good)
pans(nf(sol[1,:]))
