from common import *
from fractions import Fraction

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits += "๐๐๐๐๐๐๐๐๐ ๐ก๐ธ๐นโ๐ป๐ผ๐ฝ๐พโ๐๐๐๐๐โ๐โโโ๐๐๐๐๐๐๐โค๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐ช๐ซ"
digits += "๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐ช๐ซ๐ฌ๐ญ๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ"
digits += "โ โกโขโฃโคโฅโฆโงโจโถโทโธโนโบโปโผโฝโพโฟโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ โกโขโฃโคโฅโฆโงโจโฉ"
digits += "๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ"
digits += "๐ฌ๐ญ๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐"

def basestr(b, x, makes=True) :
    if x >= 1 :
        raise ValueError("Value must be fractional")
    if b > len(digits) and makes :
        raise ValueError("Not enough digits to handle base " + str(b))

    infe = False
    dns = set()
    bs = "0."
    for e in range(1,120+1) :
        dv = Fraction(1,b**e)
        dn = x / dv
        #print(x, dv, dn, int(dn))

        # Are we an infinite decimal?
        if dn in dns :
            infe = True
        dns.add(dn)
            
        if dn < 1 :
            if makes :
                bs += "0"
        else :
            if makes :
                bs += digits[int(dn)]
            x = x - int(dn)*dv
        # Does the expansion terminate here?
        if int(dn) == dn :
            break
    else :
        if not infe :
            infe = "Prob"

    return (infe, bs)
    
v = Fraction(1,10890)
b = 2
while True :
    (infe, des) = basestr(b, v)
    print(infe, des)
    if not infe :
        break
    b += 1

pans(b)
