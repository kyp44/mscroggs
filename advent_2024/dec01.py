from common import *

for ns in it.combinations(range(1, 16+1), r=5):
    if sum(ns) == 16:
        print(f"Numbers: {ns}, sum: {sum(ns)}, product: {product(ns)}")
