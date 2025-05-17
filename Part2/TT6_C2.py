#Sinh số PRNG
import TT1_C2
import TT5_C2
from random import getrandbits

def gener_PRNG(k,t,b):
    while True:
        check = True
        num = getrandbits(k)
        lst_nt_B = TT1_C2.Eratos2(b)
        for i in lst_nt_B:
            if num % i == 0:
                check = False
                break
        if check == True:
            if TT5_C2.Mileer_Rabin(num,t):
                return num

        
        