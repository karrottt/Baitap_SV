from student import SinhVien
import os
import pickle

def ghi_sinhvien(thumuc: str, ten_taptin: str, obj: SinhVien):
    try:
        with open(os.path.join(thumuc, te   n_taptin), 'wb') as f:
            pickle.dump(obj, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print('Xay ra loi trong qua trinh ghi file')

def doc_sinhvien(thumuc: str, ten_taptin: str):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def main():
    sv = [SinhVien('Huan Hoa Hoe', 2004, 10),
          SinhVien('Ngo Ba Kha', 2004, 7),
          SinhVien('Diep Lien Tu', 2004, 5),
          SinhVien('Dat 1 Lit', 2004, 8)]
    path = 'D:/data'
    filename = 'sinhvien2.dat'
    ghi_sinhvien(path, filename, sv)
    noidung = doc_sinhvien(path, filename)
    print(noidung)
    print('Ket thuc chuong trinh')

if __name__ == '__main__':
    main()
