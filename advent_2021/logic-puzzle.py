#! /usr/bin/env python3
"""
Run with -h for a description
"""
import argparse
from collections import OrderedDict
from dataclasses import dataclass
import sqlite3 as sql
from common import *

# Parse command line arguments
parser = argparse.ArgumentParser(description="Verifies a solution to the 2021 advent logic puzzle from a deduction database.")
parser.add_argument("fname", metavar="DATABASE", type=str, help="SQLite database file to verify")
args = parser.parse_args()

class Indeterminant(Exception) :
    pass

@dataclass
class Reindeer(object) :
    test1 : int
    test2 : int
    test3 : int
    favorite : int

    def __getattribute__(self, name) :
        """
        Throw exception when a None value is accessed to
        escape the evaluation functions.
        """
        v = object.__getattribute__(self, name)
        if v is None :
            raise Indeterminant()
        return v
    
    def is_favorite(self, v) :
        return v == self.favorite

# Read in reindeer data from db
deer = OrderedDict()
con = sql.connect(args.fname)
for row in con.execute("select reindeer, test1, test2, test3, favorite from solution order by reindeer") :
    def tryval(v) :
        if type(v) is int :
            return v
        else :
            return int(v) if len(v) == 1 else None
    deer[row[0]] = Reindeer(*[tryval(v) for v in row[1:]])

# Clues
clues = OrderedDict()
clues[1] = lambda deer : deer[2].favorite == 4
clues[2] = lambda deer : deer[2].test1 == 4
clues[3] = lambda deer : deer[2].test2 == 4
clues[4] = lambda deer : deer[2].test3 == 6
clues[5] = lambda deer : len([d for d in deer.values() if not d.is_favorite(d.test3)]) == 4
clues[6] = lambda deer : deer[4].favorite in factors(607)
clues[7] = lambda deer : deer[4].test1 == deer[4].test2 and deer[4].test1 == deer[4].test3
clues[8] = lambda deer : deer[8].test1 == 3
clues[9] = lambda deer : len([d for d in deer.values() if not d.is_favorite(d.test1)]) == 2
clues[10] = lambda deer : deer[9].test1 == 6
clues[11] = lambda deer : deer[9].test2 == 5
clues[12] = lambda deer : deer[9].test3 == 1
clues[13] = lambda deer : deer[4].test2 != 9
clues[14] = lambda deer : len([d for d in deer.values() if not d.is_favorite(d.test2)]) == 2
clues[15] = lambda deer : deer[1].test1 == 1 and deer[1].test2 == 1 and deer[1].test3 == 1
clues[16] = lambda deer : len(set([d.test2 for d in deer.values()])) == 9
clues[17] = lambda deer : deer[7].test1 != 7
clues[18] = lambda deer : deer[8].test2 == 2
clues[19] = lambda deer : deer[5].test3 != 7
clues[20] = lambda deer : len([d for dn, d in deer.items() if dn == d.test3]) == 3
clues[21] = lambda deer : deer[7].test3 in factors(148)
clues[22] = lambda deer : deer[7].test3 != 1
clues[23] = lambda deer : len([d for d in deer.values() if d.test3 == 2]) == 0
clues[24] = lambda deer : deer[7].test1 != 9

# Evaluate clues
failed = 0
indet = 0
for cn, cf in clues.items() :
    try :
        if not cf(deer) :
            failed += 1
            print("Clue", cn, "is not satisfied!")
    except Indeterminant :
        indet += 1
        print("Clue", cn, "is indeterminant")

if failed > 0 or indet > 0 :
    print(failed, "clues failed and", indet, "were indeterminant")
else :
    print("All clues were satisfied!")
