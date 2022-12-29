import os
import pickle

class NhanVien:
    def __init__(self, hoten, tuoi, luong):
        self.hoten = hoten
        self.tuoi = tuoi
        self.luong = luong

    def __str__ (self)  -> str:
        massage = '[Ho ten: ' + self.hoten + '; Tuoi: ' + str(self.tuoi) + '; Luong: ' + str(self.luong) + ']'
        return massage

#Viết hàm nhập dữ liệu cho 1 list các đối tượng thuộc lớp NhanVien
    def nhap_nhanvien(ds):
        # Nhập số lượng nhân viên
        n = int(input("Nhap so luong nhan vien: "))
        # Nhập thông tin từng nhâ   n viên
        for i in range(n):
            print("%s." %(i+1))
            hoten = input("Nhap ho ten nhan vien: ")
            tuoi = int(input("Nhap tuoi nhan vien: "))
            luong = float(input("Nhap luong nhan vien: "))
            nv = NhanVien(hoten, tuoi, luong)
            ds.append(nv)
        return ds

#Viết hàm hiển thị list các đối tượng thuộc lớp NhanVien ra màn hình
    def hien_thi_danh_sach_nhan_vien(ds):
        for nv in ds:
            print('[Ho ten: ' + nv.hoten + '; Tuoi: ' + str(nv.tuoi) + '; Luong: ' + str(nv.luong) + ']')

#Viết hàm sắp xếp list các đối tượng thuộc lớp NhanVien theo chiều giảm dần của độ tuổi
    def __gt__ (self, obj):
        return (self.tuoi > obj.tuoi)

#Viết hàm lưu list các đối tượng thuộc lớp NhanVien vào tập tin nhị phân
    def ghi_sinhvien(path: str, filename: str, ds):
        try:
            #mo file che do ghi tiep o dang nhi phan
            with open(os.path.join(path, filename), 'ab') as f:
                pickle.dump(ds, f)
            print('\nHoan thanh qua trinh ghi du lieu vao tap tin')
        except Exception as e:
            print('\nXay ra loi trong qua trinh ghi file:', e)

#Viết hàm đọc list các đối tượng thuộc lớp NhanVien từ tập tin nhị phân
    def doc_sinhvien(path: str, filename: str):
        try:
            with open(os.path.join(path, filename), 'rb') as f:
                sv = pickle.load(f)
            return sv
        except Exception as e:
            return None

