from common import *

(N, M) = (2, 19)

print(N*(N+1)*M*(M+1) % 4)
pans(N*(N+1)*M*(M+1) // 4)
