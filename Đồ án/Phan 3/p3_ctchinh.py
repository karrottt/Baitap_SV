from p3_ham import NhanVien

ds = []
#Nhap danh sach nhan vien
NhanVien.nhap_nhanvien(ds)

#NhanVien.hien_thi_danh_sach_nhan_vien(ds)
print("\nDanh sach nhan vien:")
NhanVien.hien_thi_danh_sach_nhan_vien(ds)

#Sap xep va hien thi danh sach nhan vien theo do tuoi giam dan
print("\nDanh sach nhan vien sau khi sap xep:")
sx = sorted(ds)
sx = list(reversed(sx))
for item in sx:
    print(item)

#Nhap duong dan va ten tap tin
print("\nLuu list sinh vien vao tap tin nhi phan.")
path = input("\nNhap duong dan: ")
filename = "%s.dat" %input("Nhap ten thuc muc: ")

#Luu danh sach nhan vien vao tap tin nhi phan
NhanVien.ghi_sinhvien(path, filename, ds)

#Doc danh sach tu tap tin nhi phan
print("\nDoc list sinh vien tu tap tin nhi phan.")
noidung = NhanVien.doc_sinhvien(path, filename)
for item in noidung:
    print(item)


#Ket thuc
print("\nKet thuc chuong trinh")




