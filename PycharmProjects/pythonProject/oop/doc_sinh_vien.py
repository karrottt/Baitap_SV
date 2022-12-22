import os.path

from student import SinhVien
import pickle

#Duong dan tap tin
path = 'D:/data'
filename = 'sinhvien.dat'

#Doc du lieu
with open(os.path.join(path, filename), 'rb') as f:
    sv = pickle.load(f)
print(type(sv))
print(sv)
print('Ket thuc qua trinh doc du lieu')
