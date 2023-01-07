from p2c2_ham import *

while True:
    print("****************CHƯƠNG TRÌNH CHÍNH****************")
    print("**  a. Giải hệ phương trình.                    **")
    print("**  b. Tính giới hạn.                           **")
    print("**  c. Tính đạo hàm.                            **")
    print("**  d. Tính nguyên hàm.                         **")
    print("**  e. Tính tích phân.                          **")
    print("**  f. Thoát.                                   **")
    print("**************************************************")
    key = input("Nhập tùy chọn: ")
    if key == "a":
        print("\na. Giải hệ phương trình.")
        a1 = float(input("Nhập hệ số a1: "))
        b1 = float(input("Nhập hệ số b1: "))
        c1 = float(input("Nhập hệ số c1: "))
        vp1 = float(input("Nhập vế phải 1: "))
        a2 = float(input("Nhập hệ số a2: "))
        b2 = float(input("Nhập hệ số b2: "))
        c2 = float(input("Nhập hệ số c2: "))
        vp2 = float(input("Nhập vế phải 2: "))
        a3 = float(input("Nhập hệ số a3: "))
        b3 = float(input("Nhập hệ số b3: "))
        c3 = float(input("Nhập hệ số c3: "))
        vp3 = float(input("Nhập vế phải 3: "))
        pt_nhieuan(a1, b1, c1, vp1, a2, b2, c2, vp2, a3, b3, c3, vp3)
        print("\nHoàn thành bài toán.")

    elif key == "b":
        print("\nb. Tính giới hạn.")
        f = input("Nhập hàm số: ")
        x0 = input("Nhập giới hạn hàm số: ")
        gioihan(f, x0)
        print("\nHoàn thành bài toán.")

    elif key == "c":
        print("\nc. Tính đạo hàm.")
        f = input("Nhập hàm số: ")
        daoham(f)
        print("\nHoàn thành bài toán.")

    elif key == "d":
        print("\nd. Tính nguyên hàm.")
        f = input("Nhập hàm số: ")
        nguyenham(f)
        print("\nHoàn thành bài toán.")

    elif key == "e":
        print("\ne. Tính tích phân.")
        f = input("Nhập hàm số: ")
        gh1 = input("Nhập giới hạn 1 hàm số: ")
        gh2 = input("Nhập giới hạn 2 hàm số: ")
        tichphan(f, gh1, gh2)
        print("\nHoàn thành bài toán.")

    elif key == "f":
        print("Bạn đã thoát chương trình.")
        break
    else:
        print("Vui lòng nhập lại.")
