#mã hóa rsa
import sys
sys.path.insert(0, '.\Part1')
sys.path.insert(1, '.\Part2')
from random import randint
from math import sqrt
import TT8
import TT3_C2


def private_key_RSA(q, p,e):
    n = q*p
    euler_n = (q-1)*(p-1)
    if TT8.Euclid(e,euler_n) ==1:
        print("Khóa e hợp lệ")
    d = TT8.Invert_Fp(e,euler_n)
    return [d,n]

def encode_RSA(p,q,e,plaintext):
    n = q*p
    euler_n = (q-1)*(p-1)    
    if TT8.Euclid(e,euler_n) ==1:
        print("Khóa e hợp lệ")
    ciphertext = TT3_C2.multi2_mod(plaintext,e,n)
    return ciphertext

def decode_RSA(q,p,e,ciphertext):
    priv_key = private_key_RSA(q,p,e)
    d = priv_key[0]
    n = priv_key[1]
    plaintext = TT3_C2.multi2_mod(ciphertext,d,n)
    return plaintext



