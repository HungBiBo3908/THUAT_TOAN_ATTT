# Thuật toán Miller_rabin
from TT3_C2 import multi2_mod
from random import randint

def Tach(n): #Tach n = 2^s * r 
    count = 0
    while n%2 == 0:
        count += 1
        n = int(n/2)
    return [count, n]
        
def Mileer_Rabin(n,t):
    s_r = Tach(n-1)
    s = s_r[0]
    r = s_r[1]
    lst = []
    for i in range(t):
        a = randint(2,n-1)
        while a in lst:
            a = randint(2,n-2)
        lst.append(a) 
        y = multi2_mod(a,r,n)
        if y != 1 and y != (n-1):
            j = 1
            while j<= (s-1) and y != (n-1):
                y = pow(y,2,n)
                if y == 1:
                    return False
                j +=1
            if y != (n-1):
                return False
    return True
print(Mileer_Rabin(17,5))