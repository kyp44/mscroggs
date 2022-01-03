from common import *

rows = []
k = 0
for r in range(1, 19+1) :
    row = []
    for c in range(r) :
        row.append(2*k + 1)
        k += 1
    rows.append(row)

# Test
for n in range(1, 10+1) :
    row = rows[n-1]
    print(row, np.mean(row), n**2)

pans(int(np.mean(rows[19-1])))
