#! /usr/bin/env python3
"""
Run with -h for a description
"""
import argparse
from collections import OrderedDict
from enum import Enum
import json
import roman

# Puzzle set data
fname = "puzzles.json"

# Parse command line arguments
parser = argparse.ArgumentParser(
    description="Generates LaTeX code for math puzzle questions with particular tags, or the complete set, in order. Tag data is read from '" + fname + "'.")
parser.add_argument("tags", metavar="TAGS", type=str,
                    nargs="?", help="CSV list of tags to include")
parser.add_argument("--info", "-i", action="store_true",
                    help="Show info, including available tags, question sets, and completeness of those sets.")
args = parser.parse_args()

# Set types and their labels


class SetType(Enum):
    ADVENT = "advent"
    CARD = "card"


set_type_labels = OrderedDict([
    (SetType.ADVENT, "Advent"),
    (SetType.CARD, "Card"),
])
puzzle_labels = {
    SetType.ADVENT: "Dec",
    SetType.CARD: "Problem",
}

# Available tags and their labels


class Tag(Enum):
    BASE = "base"
    BOOK = "book"
    BOX = "box"
    CALC = "calc"
    COMB = "comb"
    CONS = "cons"
    CROSS = "cross"
    DIG = "dig"
    EXP = "exp"
    FACT = "fact"
    GEOM = "geom"
    MISC = "misc"
    MOD = "mod"
    NUM = "num"
    POLY = "poly"
    PROB = "prob"
    SUM = "sum"
    TRI = "tri"


tag_labels = {
    Tag.BASE: "Number base",
    Tag.BOOK: "Book",
    Tag.BOX: "Box puzzle",
    Tag.CALC: "Calculus",
    Tag.COMB: "Combinatorics",
    Tag.CONS: "Consecutive numbers",
    Tag.CROSS: "Cross number",
    Tag.DIG: "Digits",
    Tag.EXP: "Polynomial expansion",
    Tag.FACT: "Factorial",
    Tag.GEOM: "Geometry",
    Tag.MISC: "Miscellaneous",
    Tag.MOD: "Modulo",
    Tag.NUM: "Number theory",
    Tag.POLY: "Higher degree polynomial",
    Tag.PROB: "Probability",
    Tag.SUM: "Sums",
    Tag.TRI: "Number triangle",
}

# Data classes


class Puzzle:
    def __init__(self, d):
        for f in ("number",):
            setattr(self, f, d[f] if f in d else None)
        self.tags = {Tag(t) for t in d["tags"]}


class Set:
    def __init__(self, d):
        self.type = SetType(d["type"])
        self.number = d["number"]
        for f in ("year",):
            setattr(self, f, d[f] if f in d else None)
        self.puzzles = [Puzzle(p) for p in d["puzzles"]]


# List of tags to include
if args.tags is None:
    include_tags = {t for t in Tag}
else:
    include_tags = {Tag(t) for t in args.tags.split(",")}

# Load and parse the puzzle data
with open(fname, "r") as f:
    sets = [Set(d) for d in json.load(f)]

if args.info:
    # Shoe info
    def header(s):
        div = "-"*50
        print(div, s, div)

    header("Available tags")
    for tag in Tag:
        print(tag.value + ":", tag_labels[tag])

    header("Sets")
    for sett in sets:
        # Puzzle numbers
        nums = sorted([p.number for p in sett.puzzles])
        vs = []
        if len(set(nums)) != sett.number:
            vs.append("Incomplete")
        if len(set(nums)) != len(nums):
            vs.append("Duplicates")
        elif nums != list(range(1, len(nums)+1)):
            vs.append("Missing numbers")
        print(set_type_labels[sett.type], str(sett.year) + ":", len(nums), "puzzle" + (
            "s" if len(nums) > 1 else ""), "(" + ("Complete" if len(vs) == 0 else ", ".join(vs)) + ")")
else:
    # Generate LaTeX code
    for year in sorted(set([s.year for s in sets])):
        for typ in set_type_labels.keys():
            ss = [s for s in sets if s.year == year and s.type == typ]
            if len(ss) > 1:
                raise ValueError(
                    "There are multiple " + set_type_labels[typ] + " " + str(year) + " sets!")
            for s in ss:
                for p in sorted(s.puzzles, key=lambda p: p.number):
                    if len(p.tags.intersection(include_tags)) < 1:
                        continue
                    label = set_type_labels[s.type] + " " + str(
                        s.year) + ", " + puzzle_labels[s.type] + " " + str(p.number)
                    quest = "@".join([s.type.value, roman.toRoman(s.year -
                                     2000).lower(), roman.toRoman(p.number).lower()])
                    tags = ", ".join(sorted([tag_labels[t] for t in p.tags]))
                    print(r"\puzzle{" + label + "}{\\" +
                          quest + "}{" + tags + "}")
