#Cong tru chinh xac boi

def Cong_boi(a,b,W,t):
    c_plus = [0]*t
    e = 0
    MAX = 2**W
    for i in range (t-1,-1,-1):
        c_plus[i] = a[i] + b[i] + e
        if (c_plus[i]>= MAX):
            c_plus[i] = c_plus[i] - MAX
            e = 1
        else:
            e = 0
    return [e,c_plus]

def Tru_boi(a,b,W,t):
    c_hieu = [0]*t
    e = 0
    MAX = 2**W
    for i in range (t-1,-1,-1):
        c_hieu[i] = a[i] - b[i] - e
        if (c_hieu[i] < 0):
            c_hieu[i] = c_hieu[i] + MAX
            e = 1
        else:
            e = 0
    return [e,c_hieu]

#a = [0,11,173,248]
#b = [0,1,226,64]
#w = 8
#t = 4
#
#print(Cong_boi(a,b,w))
#print(Tru_boi(a,b,w))

