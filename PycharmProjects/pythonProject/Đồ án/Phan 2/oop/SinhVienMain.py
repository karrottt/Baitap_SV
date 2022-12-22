from nhanvien import NhanVien
while (1==1):
    print("\nCHUONG TRINH QUAN LY NHAN VIEN")
    print("*************************MENU******************************")
    print("**  1. Nhap thong tin nhan vien.                         **")
    print("**  2. Hien thi thong tin tat ca nhan vien               **")
    print("**  3. Sap xep nhan vien theo do tuoi giam gian.         **")
    print("**  4. Luu thong tin nhan vien vao tap tin nhi phan.     **")
    print("**  5. Hien thi thong tin nhan vien tu tap tin nhi phan. **")
    print("**  0. Thoat                                             **")
    print("***********************************************************")

    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Nhap thong tin nhan vien.")
        NhanVien.nhapNhanVien()
        print("\nThem nhan vien thanh cong!")
    else:
        print()