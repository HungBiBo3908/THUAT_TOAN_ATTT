#Chia so ve mang va nguoc lai
import math

def BieuDien_num_to_LST(a, p, W):
    m = math.ceil(math.log2(p))
    t = math.ceil(m/W)
    lst = [None] * t
    for i in range (0,t):
        He_So = pow(2,W*(t-i-1))
        lst[i] = int(a/He_So)
        a = a - lst[i]*He_So
    return lst

#def BieuDien_LST_bit(a, p, W):
#    m = math.ceil(math.log2(p))
#    t = math.ceil(m/W)
#    lst = [None] * t
#    mask = (1 << W) - 1
#    for i in range (0,t):
#        check = a
#        lst[i] = check>>(W*(t-i-1)) & mask
#    return lst

def BieuDien_Lst_to_Num(lst: list, p, W):
    num = 0
    for i in range(len(lst)):
        num += lst[i] * pow(2, W*(len(lst)-i-1))
    return num

#p =2147483647    
#list1 = BieuDien_LST_bit(23456789,p,8)
#print(list1)
#print(BieuDien_Lst_to_Num(list1,p,8))