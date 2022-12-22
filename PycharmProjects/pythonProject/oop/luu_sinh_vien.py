import os.path

from student import SinhVien
import pickle

#Tao 1 doi tuong thuoc lop SinhVien
sv = SinhVien('Ngo Ba Kha', 2004, 10.0)

#Duong dan tap tin
path = 'D:/data'
filename = 'sinhvien.dat'

#Luu tru
with open(os.path.join(path, filename), 'wb') as f:
    pickle.dump(sv, f)
print('Ket thuc qua trinh luu du lieu')
