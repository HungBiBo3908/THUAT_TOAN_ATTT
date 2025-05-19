#DF
import sys
sys.path.insert(0,'.\Part2')
from TT3_C2 import multi2_mod
def diffe_hellman(p,g,a,b):
    A = multi2_mod(g,a,p)
    k = multi2_mod(A,b,p)
    return k
print(diffe_hellman(7,3,2,3))