from p3_ham import NhanVien

ds = []
while True:
    print("\n******************CHƯƠNG TRÌNH CHÍNH******************")
    print("**  a. Nhập danh sách nhân viên.                    **")
    print("**  b. Hiển thị danh sách nhân viên.                **")
    print("**  c. Sắp xếp và hiển thị danh sách nhân viên.     **")
    print("**  d. Lưu list.                                    **")
    print("**  e. Đọc list.                                    **")
    print("**  f. Thoát.                                       **")
    print("******************************************************")
    key = input("Nhập tùy chọn: ")
    if key == "a":
        #Nhap danh sach nhan vien
        print("a. Nhập danh sách nhân viên.")
        NhanVien.nhap_nhanvien(ds)
    elif key == "b":
        print("\nDanh sách nhân viên:")
        NhanVien.hien_thi_danh_sach_nhan_vien(ds)
    elif key == "c":
        #Sap xep va hien thi danh sach nhan vien theo do tuoi giam dan
        print("\nDanh sách nhân viên sau khi sắp xếp:")
        sx = sorted(ds)
        sx = list(reversed(sx))
        for item in sx:
            print(item)
    elif key == "d":
        #Nhap duong dan va ten tap tin
        print("\nLưu list nhân viên vào tập tin nhị phân.")
        path = input("\nNhập đường dẫn: ")
        filename = "%s.dat" %input("Nhập tên thư mục: ")

        #Luu danh sach nhan vien vao tap tin nhi phan
        NhanVien.ghi_sinhvien(path, filename, ds)

    elif key == "e":
        #Doc danh sach tu tap tin nhi phan
        print("\nĐọc list nhân viên từ tập tin nhị phân.")
        noidung = NhanVien.doc_sinhvien(path, filename)
        for item in noidung:
            print(item)
    elif key == "f":
        #Ket thuc
        print("\nKết thúc chương trình.")
        break
    else:
        print("Vui lòng nhập lại.")




