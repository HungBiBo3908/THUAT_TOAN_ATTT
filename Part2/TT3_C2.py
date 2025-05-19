# Bình phương có lặp (a^p mod n)
from math import log2
def nhi_phan(p):
    length = int(log2(p)) + 1
    lst = []
    for i in range(length):
        lst.append(p%2)
        p = p//2
    return lst
def multi2_mod(a,p,n):
    b = 1
    if p == 0:
        return b
    A = a
    lst_k = nhi_phan(p)
    if lst_k[0] == 1:
        b = a
    for i in range(1,len(lst_k)):
        A = pow(A,2,n)
        if lst_k[i] == 1:
            b = pow(A*b,1,n)
    return b