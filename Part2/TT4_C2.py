#Check so nguyeen to Fermat voi co so a co t buoc an toan
import TT3_C2
from random import randint

def fermat(n,t):
    lst = []
    for i in range(t):
        a = randint(2,n-1)
        while a in lst:
            a = randint(2,n-2)
        lst.append(a)
        r = TT3_C2.multi2_mod(a,n-1,n)
        if r != 1:
            return False
    return True
