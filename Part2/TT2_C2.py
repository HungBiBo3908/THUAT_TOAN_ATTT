#phân tích thừa số nguyên tố
import TT1_C2
from Part1.TT8 import Euclid
from math import sqrt

def factor(number):
    lst = TT1_C2.Eratos2(int(sqrt(number)))
    list_factor = []
    for i in lst:
        while number % i == 0:
            list_factor.append(i)
            number = number//i
        if number == 1:
            break
    if number != 1: list_factor.append(number)
    return list_factor

def Pollard_Rho(n,c = 1):
    a = 2
    b = 2
    while True:
        a = (a*a +c)%n
        b = (b*b + c)%n
        b = (b*b + c)%n
        d = Euclid(a-b,n)
        if d>1 and d<n:
            return d
        if d == n:
            return 0