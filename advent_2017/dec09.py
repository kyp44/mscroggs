from common import *
ds = tuple(range(1,15+1))

rs = []
while True :
    rs.append(ds)
    print(ds)
    if len(ds) < 2 :
        break
    ds = ds[1:-1]

pans(sum([sum(r) for r in rs]))
