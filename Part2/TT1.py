# Sàng eratosthenes
from sympy import sqrt,ceiling

def Eratos(last):
    a = [True] *(last+1)
    a[0],a[1] = False, False
    check_del = int(sqrt(last))
    for i in range(2,check_del+1):
        for j in range(2*i,last+1,i):
            a[j] = False
    return a

def Eratos2(last):
    last = 30
    check_del = int(sqrt(last))
    c = [2]
    count = 0
    for i in range (0,last+1,check_del):
        check_max = i+check_del
        if check_max >= last: check_max = last+1
        a = [t for t in range(i,check_max)]
        check = int(sqrt(i+check_del - 1))
        for j in c:
            if j <= check:
                m = int((i+check_del-1)/j)
                n = ceiling(i/j)
                for k in range(n,m+1):
                    a[j*k-check_del*count] = 0
            else: break
        for j in a:
            if j != 0 and j != 1: c.append(j)
        count += 1