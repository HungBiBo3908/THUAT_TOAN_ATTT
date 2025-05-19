#Gp
import sys
sys.path.insert(1, '.\Part1')
from TT8 import Invert_Fp, Euclid

def invert(a,p):
    if Euclid(a,p)!= 1:
        return "Khong ton tai"
    else:
        return Invert_Fp(a,p)