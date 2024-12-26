from common import *
from dataclasses import dataclass

santa = 444


@dataclass
class Elf:
    three: int
    one: int


elves = [
    Elf(138, 4),
    Elf(495, 3),
    Elf(144, 8),
]

code = santa
for elf in elves:
    code -= elf.three
    code *= elf.one

print("Code:", code)
