from sympy import sqrt, ceiling

def Eratos(last):
    a = [True] *(last+1)
    lst_priv = []
    chia_list = int(sqrt(last))
    for i in range(2,chia_list+1):
        for j in range(2*i,last+1,i):
            a[j] = False
    for i in range(2,last+1):
        if a[i] == True:
            lst_priv.append(i)
    return lst_priv

def Eratos2(last):
    chia_list = int(sqrt(last))
    count = 1
    c = Eratos(chia_list-1)
    for i in range (chia_list,last+1,chia_list): #chạy từng cặp (chia_list) số từ 0 đến last
        check_max = i+chia_list
        if check_max > last: check_max = last+1
        a = [t for t in range(i,check_max)] #1 mảng chỉ chứa 1 bộ chia_list số liên tục
        check_q = int(sqrt(check_max - 1))
        for j in c:
            if j <= check_q: 
                m = int((check_max-1)/j)
                n = ceiling(i/j)
                for k in range(n,m+1): #chặn đầu đít của bội số nguyên tố trong bộ số a.
                    a[j*k-chia_list*count] = 0 #sửa hết phần tử là bội thành 0
            else: break
        for j in a:
            if j != 1 and j!= 0:
                c.append(j)
        count += 1
    return c