#tính nghịch đảo và UCLN
#thuật toán cần xem loại x1%p chưa tối ưu

def EClide_Pro(a0,b0):
    if b0 > a0:
        tmp = a0
        a0 = b0
        b0 = tmp
    if b0 == 0: return [0,1,0]
    a,b,d,x,y,x2, x1, y2, y1 = a0,b0, 0,0,0,1,0,0,1
    while b>0:
        q = int(a/b)
        r = a-q*b
        x = x2 - q*x1
        y = y2-q*y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1 
        y1 = y 
    d,x,y = a,x2,y2
    if d == 1:
        return("UCLN {0}, {1} la {2}\nnghich dao của {0} mod {1} la {3}\nnghich dao cua {1} mod {0} là {4}".format(a0,b0,d,x,y))
    else:
        return("UCLN: ",d)
    
def Invert_Fp(a,p):
    u = a
    v = p
    x1,x2 = 1, 0
    while u != 1:
        q = int(v/u)
        r = v - q*u
        x = x2 - q*x1
        v = u
        u = r
        x2 = x1
        x1 = x
    if x1 < 0:
        return x1 + p
    return x1

def Euclid(a,b):
    if a < b:
        tmp = a 
        a = b
        b = tmp
    while b > 0:
        r = a % b
        a = b
        b = r
    return a
#print(Invert_Fp(8,31))
#print(EClide_Pro(1759,550))