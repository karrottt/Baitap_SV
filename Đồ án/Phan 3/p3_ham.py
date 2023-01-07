import os
import pickle

class NhanVien:
    def __init__(self, hoten, tuoi, luong):
        self.hoten = hoten
        self.tuoi = tuoi
        self.luong = luong

    def __str__ (self)  -> str:
        massage = "[Họ tên: " + self.hoten + "; Tuổi: " + str(self.tuoi) + "; Lương: " + str(self.luong) + "]"
        return massage

#Viet ham nhap du lieu cho 1 list cac doi tuong thuoc lop NhanVien
    def nhap_nhanvien(ds):
        #Nhap so luong nhan vien
        n = int(input("Nhập số lượng nhân viên: "))
        #Nhap so luong nhan vien
        for i in range(n):
            print("%s." %(i+1))
            hoten = input("Nhập họ tên nhân viên: ")
            tuoi = int(input("Nhập tuổi nhân viên: "))
            luong = float(input("Nhập lương nhân viên: "))
            nv = NhanVien(hoten, tuoi, luong)
            ds.append(nv)
        return ds

#Viet ham hien thi list cac doi tuong thuoc lop NhanVien ra man hinh
    def hien_thi_danh_sach_nhan_vien(ds):
        for nv in ds:
            print("[Họ tên: " + nv.hoten + "; Tuổi: " + str(nv.tuoi) + "; Lương: " + str(nv.luong) + "]")

#Viet ham sap xep list cac doi tuong thuoc lop NhanVien theo chieu giam dan cua do tuoi
    def __gt__ (self, obj):
        return (self.tuoi > obj.tuoi)

#Viet ham luu list cac doi tuong thuoc lop NhanVien vao tap tin nhi phan
    def ghi_sinhvien(path: str, filename: str, ds):
        try:
            #Mo file che do ghi tiep o dang nhi phan
            with open(os.path.join(path, filename), "ab") as f:
                pickle.dump(ds, f)
            print("\nHoàn thành quá trình ghi dữ liệu vào tập tin.")
        except Exception as e:
            print("\nXảy ra lỗi trong quá trình ghi tập tin: %s." %e)

#Viet ham doc list cac doi tuong thuoc lop NhanVien tu tap tin nhi phan
    def doc_sinhvien(path: str, filename: str):
        try:
            with open(os.path.join(path, filename), "rb") as f:
                sv = pickle.load(f)
            return sv
        except Exception as e:
            print("\nXảy ra lỗi trong quá trình đọc tập tin: %s." %e)

