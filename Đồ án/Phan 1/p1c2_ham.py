import numpy as np
import os
import pickle

#sinh ngau nhien cac gia tri cho 1 list cac so thuc trong khoang [a, b]
def sinhlist(a: float, b: float, n: int) :
    if a < b:
        v = (b -a)*np.random.random_sample(n) + a
        print(v)
        return(v)
    else:
        print("Nhap a < b")

#sap xep list
def sapxep(reverse, ds):
    if reverse == True:
        sx = sorted(list)
        print("Sap xep theo chieu tang dan:", sx)
    else:
        sx = list(reversed(sorted(ds)))
        print("Sap xep theo chieu giam dan:", sx)
    return sx

#tim kiem so n trong list
def timkiem(n, ds):
    if n in ds:
        vitri = []
        for i in range(0, len(ds)):
            if ds[i] == n:
                vitri.append(i)
        print("Tim thay so %s tai vi tri: %s" % (n, vitri))
    else:
        print("Khong tim thay so %s trong danh sach" % n)

#luu list vao tap tin tap tin van ban hay tap tin nhi phan
def luu_taptin(kieu_taptin, thumuc, ten_taptin, ds):
    if kieu_taptin == "vanban":
        try:
            with open(os.path.join(thumuc, ten_taptin), 'w') as f:
                f.write(str(ds))
            print('\nHoan thanh qua trinh ghi du lieu vao tap tin')
        except Exception as e:
            print('\nXay ra loi trong qua trinh ghi file: ', e)
    else:
        try:
            with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
                pickle.dump(ds,  f)
            print('\nHoan thanh qua trinh ghi du lieu vao tap tin')
        except Exception as e:
            print('\nXay ra loi trong qua trinh ghi file: ', e)
