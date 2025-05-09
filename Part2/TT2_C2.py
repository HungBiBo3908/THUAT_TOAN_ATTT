#phân tích thừa số nguyên tố
import TT1_C2

def factor(number):
    lst = TT1_C2.Eratos2((number))
    lst.reverse()
    list_factor = []
    for i in lst:
        while number % i == 0:
            list_factor.append(i)
            number = number/i
        if number == 1:
            break
    return list_factor

