#rabin

import sys
sys.path.insert(0, '.\Part1')
sys.path.insert(1, '.\Part2')
from random import randint
from math import sqrt
import TT8
import TT3_C2

def encode_rabin(q,p,m):
    if (q % 100) % 4 == 3 and (p % 100) % 4 == 3:
        print("q,p pass")
        n = q*p
    c = TT3_C2.multi2_mod(m,2,n)
    return c
print(encode_rabin(7,11,9))