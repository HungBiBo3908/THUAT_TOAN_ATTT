#vet can
from TT0_C3 import tach_chuoi
def vet_can(a,b):
    lst_a = tach_chuoi(a)
    lst_b = tach_chuoi(b)
    for i in range(len(lst_a)):
        a = False
        for j in range(len(lst_b)):
            if i+j > len(lst_a)-1:
                return " Không tìm thấy"
            if lst_b[j] == lst_a[i+j]:
                a = True
            else:
                a = False
                break
        if  a == True:
            return i