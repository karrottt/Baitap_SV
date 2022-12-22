from student import SinhVien
import os
import pickle

def ghi_sinhvien(thumuc: str, ten_taptin: str, objs: list[SinhVien]):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'w') as f:
            pickle.dump(objs, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print(e)
        print('Xay ra loi trong qua trinh ghi file')

def doc_sinhvien(thumuc: str, ten_taptin: str) -> list[SinhVien]:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def in_list_sinhvien(content: list[SinhVien]):
    for item in content:
        print(item)


def main():
    sv = [SinhVien('Huan Hoa Hoe', 2004, 10),
          SinhVien('Ngo Ba Kha', 2004, 7),
          SinhVien('Diep Lien Tu', 2004, 5),
          SinhVien('Dat 1 Lit', 2004, 8)]
    path = 'D:/data'
    filename = 'sinhvien2.dat'
    ghi_sinhvien(path, filename, sv)
    noidung = doc_sinhvien(path, filename)
    in_list_sinhvien(noidung)
    print('Ket thuc chuong trinh')

if __name__ == '__main__':
    main()
