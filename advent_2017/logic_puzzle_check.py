from enum import Enum

# Actual solution
PA = 3
PB = 5
PC = 4

HA = 1
HB = 8
HC = 2

FE = 495
FO = 497

class Shoes(Enum) :
    BLUE = 1
    RED = 2

class Shirt(Enum) :
    WHITE = 1
    PINK = 1

class Hat(Enum) :
    GREEN = 1
    ORANGE = 2

class Trousers(Enum) :
    GREY = 1
    PURPLE = 2

even = (Shoes.BLUE, Shirt.PINK, Hat.GREEN, Trousers.GREY)
odd = (Shoes.RED, Shirt.WHITE, Hat.ORANGE, Trousers.PURPLE)
    
def says(dn, elf, sm) :
    c = False
    if dn % 2 == 0 :
        if sm :
            c = elf in even
        else :
            c =  elf in odd
    else :
        if sm :
            c =  elf in odd
        else :
            c =  elf in even

    if not c :
        print("Uh oh! Violation of day", dn, "statement!")

# Verify statements
says(1, Shoes.RED, PA in (1, 2, 3))
says(2, Shoes.RED, PA in (1, 2, 4))
says(3, Shirt.WHITE, HA in (1, 2, 6))
says(4, Shoes.BLUE, FE == 495)
says(5, Shoes.RED, HA in (1, 6, 9))
says(6, Shirt.PINK, HB != 6)
says(7, Hat.GREEN, HB in (3, 4))
says(8, Shoes.RED, set((PA, PB, PC)) == set((5, 2, 9)))
says(9, Shoes.BLUE, HB in (5, 1, 2))
says(10, Hat.ORANGE, FO == 249)
says(11, Shirt.WHITE, FO == 497)
says(12, Trousers.GREY, HA in (3, 1, 5))
says(13, Hat.GREEN, 7 in (HA, HB, HC))
says(14, Shirt.PINK, 8 in (HA, HB, HC))
says(15, Shoes.BLUE, HC in (9, 6, 8))
says(16, Shoes.BLUE, PB in (5, 7, 0))
says(17, Trousers.GREY, PA == 1)
says(18, Hat.GREEN, PB in (1, 5, 4))
says(19, Trousers.PURPLE, HC in (2, 6, 8))
says(20, Hat.ORANGE, PC == 2)
says(21, Shirt.WHITE, PC in (4, 9, 6))
says(22, Trousers.PURPLE, 294 % PC == 0)
says(23, Shoes.RED, 120 % PC == 0)
says(24, Hat.GREEN, PA*PB*PC*HA*HB*HC == 960)
