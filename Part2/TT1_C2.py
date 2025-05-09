# Sàng eratosthenes
from sympy import sqrt,ceiling

def Eratos(last):
    a = [True] *(last+1)
    a[0],a[1] = False, False
    chia_list = int(sqrt(last))
    for i in range(2,chia_list+1):
        for j in range(2*i,last+1,i):
            a[j] = False
    return a

