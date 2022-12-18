import numpy as np
import os
import pickle

#sinh ngau nhien cac gia tri cho 1 list cac so thuc trong khoang [a, b]
def sinhlist(a, b, n):
    if a < b:
        global v
        v = (b -a)*np.random.random_sample(n) + a
        print(v)
    else:
        print("Nhap a < b")

#sap xep list
def sapxep(reverse):
    if reverse == True:
        sx = sorted(v)
        print("Sap xep theo chieu tang dan:", sx)
    else:
        sx = list(reversed(sorted(v)))
        print("Sap xep theo chieu giam dan:", sx)

#tim kiem so n trong list
def timkiem(n):
    if n in v:
        vitri = []
        for i in range(0, len(v)):
            if v[i] == n:
                vitri.append(i)
        print("Tìm thấy số %s tại vị trí: %s" % (n, vitri))
    else:
        print("Không tìm thấy số %s trong danh sách" % n)

#luu list vao tap tin tap tin van ban hay tap tin nhi phan
def luu_taptin(kieu_taptin, thumuc, ten_taptin):
    if kieu_taptin == "vanban":
        try:
            with open(os.path.join(thumuc, ten_taptin), 'w') as f:
                pickle.dump(v, f)
            print('Hoan thanh qua trinh ghi du lieu vao tap tin')
        except Exception as e:
            print('Xay ra loi trong qua trinh ghi file')
    else:
        try:
            with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
                pickle.dump(v, f)
            print('Hoan thanh qua trinh ghi du lieu vao tap tin')
        except Exception as e:
            print('Xay ra loi trong qua trinh ghi file')