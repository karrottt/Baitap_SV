from p1c2_ham import *

while True:
    print("****************CHUONG TRINH CHINH****************")
    print("**  a. Sinh ngau nhien list cac so thuc.        **")
    print("**  b. Luu list vao tap tin van ban.            **")
    print("**  c. Sap xep list theo chieu giam dan.        **")
    print("**  d. Luu list o cau c vao tap tin van ban.    **")
    print("**  e. Tim kiem so n trong list o dau d.        **")
    print("**  f. Thoat                                    **")
    print("**************************************************")

    key = input("Nhap tuy chon: ")
    if key == "a":
        print("\na. Sinh ngau nhien list cac so thuc trong [a, b].")
        a = float(input("Nhap so a: "))
        b = float(input("Nhap so b: "))
        n = int(input("Sinh ngau nhien list cac so thuc gom bao nhieu so? "))
        print("\nList %s so thuc trong khoang [%s, %s] la: " %(n, a, b))
        v = sinhlist(a, b, n)
        print("\nSinh list thanh cong!")

    elif key == "b":
        print("\nb. Luu list vao tap tin van ban.")
        kieu_taptin = "vanban"
        thumuc = input("Nhap duong dan luu tap tin: ")
        ten_taptin = input("Nhap ten tap tin: ")
        luu_taptin(kieu_taptin, thumuc, ten_taptin, v)

    elif key == "c":
        print("\nc. Sap xep list theo chieu giam dan.")
        reverse = False
        c = sapxep(reverse, v)
        print("\nSap xep thanh cong!")

    elif key == "d":
        print("\nd. Luu list o cau c vao tap tin van ban.")
        kieu_taptin = "vanban"
        thumuc = input("Nhap duong dan luu tap tin: ")
        ten_taptin = input("Nhap ten tap tin: ")
        luu_taptin(kieu_taptin, thumuc, ten_taptin, c)

    elif key == "e":
        print("\ne. Tim kiem so n trong list o dau d.")
        n = float(input("Nhap so n: "))
        timkiem(n, c)

    elif key == "f":
        print("Ban da thoat chuong trinh.")
        break
    else:
        print("Vui long nhap lai.")

