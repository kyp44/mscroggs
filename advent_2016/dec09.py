from common import *

removed = [
    (4, 1),
    (4, 2),
    (5, 4),
    (5, 5),
    (6, 1),
    (6, 2),
    (7, 1),
    (7, 2),
    (9, 4),
    (9, 5),
    (10, 4),
    (10, 5),
]

pans(GridRoutes((11, 6), removed=removed).routes())
