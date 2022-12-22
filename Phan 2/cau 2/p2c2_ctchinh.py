from p2c2_ham import *

while True:
    print("****************CHUONG TRINH CHINH****************")
    print("**  a. Giai he phuong trinh.                    **")
    print("**  b. Tinh gioi han.                           **")
    print("**  c. Tinh dao ham.                            **")
    print("**  d. Tinh  nguyen ham.                        **")
    print("**  e. Tinh tich phan.                          **")
    print("**  f. Thoat                                    **")
    print("**************************************************")
    key = input("Nhap tuy chon: ")
    if key == "a":
        print("\na. Giai he phuong trinh.")
        a1 = float(input("Nhap he so a1: "))
        b1 = float(input("Nhap he so b1: "))
        c1 = float(input("Nhap he so c1: "))
        vp1 = float(input("Nhap he so vp1: "))
        a2 = float(input("Nhap he so a2: "))
        b2 = float(input("Nhap he so b2: "))
        c2 = float(input("Nhap he so c2: "))
        vp2 = float(input("Nhap he so vp2: "))
        a3 = float(input("Nhap he so a3: "))
        b3 = float(input("Nhap he so b3: "))
        c3 = float(input("Nhap he so c3: "))
        vp3 = float(input("Nhap he so vp3: "))
        pt_nhieuan(a1, b1, c1, vp1, a2, b2, c2, vp2, a3, b3, c3, vp3)
        print("\nHoan thanh bai toan.")

    elif key == "b":
        print("\nb. Tinh gioi han.")
        f = input("Nhap ham so: ")
        x0 = input("Nhap gioi han ham so: ")
        gioihan(f, x0)
        print("\nHoan thanh bai toan.")

    elif key == "c":
        print("\nc. Tinh dao ham.")
        f = input("Nhap ham so: ")
        daoham(f)
        print("\nHoan thanh bai toan.")

    elif key == "d":
        print("\nd. Tinh  nguyen ham.")
        f = input("Nhap ham so: ")
        nguyenham(f)
        print("\nHoan thanh bai toan.")

    elif key == "e":
        print("\ne. Tinh tich phan.")
        f = input("Nhap ham so: ")
        gh1 = input("Nhap gioi han 1 ham so: ")
        gh2 = input("Nhap gioi han 2 ham so: ")
        tichphan(f, gh1, gh2)
        print("\nHoan thanh bai toan.")

    elif key == "f":
        print("Ban da thoat chuong trinh.")
        break
    else:
        print("Vui long nhap lai.")
