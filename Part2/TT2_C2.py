#phân tích thừa số nguyên tố
import TT1_C2
from math import sqrt

def factor(number):
    lst = TT1_C2.Eratos2(int(sqrt(number)))
    lst.reverse()
    list_factor = []
    for i in lst:
        while number % i == 0:
            list_factor.append(i)
            number = number/i
        if number == 1:
            break
    if number != 1: list_factor.append(int(number))
    return list_factor
print(factor(223556))
