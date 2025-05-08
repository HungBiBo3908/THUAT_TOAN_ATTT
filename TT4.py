#phép nhân

from math import ceil,log2
import TT1

def Multi(a,b,p,W):
    t = ceil(log2(p)/W)
    c = [0] * 2*t
    if type(a)!= list:
        a = TT1.BieuDien_num_to_LST(a,p,W)
    if type(b) != list:
        b = TT1.BieuDien_num_to_LST(b,p,W)
    a = a[::-1]
    b = b[::-1]
    for i in range(t):
        u = 0
        for j in range (t):
            pre_u_v = c[i+j] + a[i]*b[j] + u  
            v = pre_u_v& ((1<<W)-1)
            u = pre_u_v >>W    
            c[i+j] = v
        c[i+t] = u
    return c[::-1]
#a = [0,11,173,248]
#b = [0,1,226,64]
#p = 2147483647
#W = 8
#print(Multi(a,b,p,W))
