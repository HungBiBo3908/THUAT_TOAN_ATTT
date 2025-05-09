# Cộng trừ trên trường Fp
import math
import TT1
import TT2

def Cong_Fp(a,b,p,W):
    Plus_Fp = []
    m = math.ceil(math.log2(p))
    t = math.ceil(m/W)
    if (type(a) != list):
        a = TT1.BieuDien_num_to_LST(a,p,W)
    if (type(b) != list):
        b = TT1.BieuDien_num_to_LST(b,p,W)
    c = TT2.Cong_boi(a,b,W,t)
    if c[0] == 1:
        p = TT1.BieuDien_num_to_LST(p,p,W)
        Plus_Fp = TT2.Tru_boi(c[1],p,W,t)
    else:
        m = TT1.BieuDien_Lst_to_Num(c[1],p,W)
        if m > p: 
            m = m - p
        Plus_Fp = TT1.BieuDien_num_to_LST(m,p,W)
    return Plus_Fp

def Tru_Fp(a,b,p,W):
    m = math.ceil(math.log2(p))
    t = math.ceil(m/W)
    if (type(a) != list):
        a = TT1.BieuDien_num_to_LST(a,p,W)
    if (type(b) != list):
        b = TT1.BieuDien_num_to_LST(b,p,W)
    Tru_Fp = []
    c = TT2.Tru_boi(a,b,W,t)
    if c[0] == 1:
        p = TT1.BieuDien_num_to_LST(p,p,W)
        Tru_Fp = TT2.Cong_boi(c[1],p,W,t)
        return Tru_Fp[1]
    return c[1]