import numpy as np
import os
import pickle

#Sinh ngau nhien cac gia tri cho 1 list cac so thuc trong khoang [a, b]
def sinhlist(a: float, b: float, n: int):
    if a < b:
        v = (b -a)*np.random.random_sample(n) + a
        print(v)
        return(v)
    else:
        print("Vui lòng nhập a < b.")

#sap xep list
def sapxep(reverse, ds):
    if reverse == True:
        sx = sorted(list)
        print("Sắp xếp theo chiều tăng dần: %s." %sx)
    elif reverse == False:
        sx = list(reversed(sorted(ds)))
        print("Sắp xếp theo chiều giảm dần: %s." %sx)
    else:
        print("Vui lòng nhập lại tham số reverse.")
    return sx

#tim kiem so n trong list
def timkiem(n, ds):
    if n in ds:
        vitri = []
        for i in range(0, len(ds)):
            if ds[i] == n:
                vitri.append(i)
        print("Tìm thấy số %s tại vị trí: %s." % (n, vitri))
    else:
        print("Không tìm thấy số %s trong danh sách." % n)

#luu list vao tap tin tap tin van ban hay tap tin nhi phan
def luu_taptin(filetype, path, filename, ds):
    if filetype == "vanban":
        try:
            with open(os.path.join(path, filename), 'w') as f:
                f.write(str(ds))
            print("\nHoàn thành quá trình ghi dữ liệu vào tập tin.")
        except Exception as e:
            print("\nXảy ra lỗi trong quá trình ghi tập tin: %s." %e)
    elif filetype == "nhiphan":
        try:
            with open(os.path.join(path, filename), 'wb') as f:
                pickle.dump(ds,  f)
            print("\nHoàn thành quá trình ghi dữ liệu vào tập tin.")
        except Exception as e:
            print("\nXảy ra lỗi trong quá trình ghi tập tin: %s." %e)
    else:
        print("Vui lòng nhập lại.")
