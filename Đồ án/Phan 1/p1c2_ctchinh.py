from p1c2_ham import *

while True:
    print("\n****************CHƯƠNG TRÌNH CHÍNH****************")
    print("**  a. Sinh ngẫu nhiên list các số thực.        **")
    print("**  b. Lưu list vào tập tin văn bản.            **")
    print("**  c. Sắp xếp list theo chiều giảm dần.        **")
    print("**  d. Lưu list ở câu (c) vào tập tin văn bản.  **")
    print("**  e. Tìm kiếm số n trong list ở câu (d).      **")
    print("**  f. Thoát                                    **")
    print("**************************************************")

    key = input("Nhập tùy chọn: ")
    if key == "a":
        print("\na. Sinh ngẫu nhiên list các số thực trong khoảng [a, b].")
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        n = abs(int(input("Sinh ngẫu nhiên list các số thực gồm bao nhiêu số? ")))
        print("\nList %s số thực trong khoảng [%s, %s] là: " %(n, a, b))
        v = sinhlist(a, b, n)
        print("\nSinh list thành công!")

    elif key == "b":
        print("\nb. Lưu list vào tập tin văn bản.")
        filetype = "vanban"
        path = input("Nhập đường dẫn lưu tập tin: ")
        filename = input("Nhập tên tập tin: ")
        luu_taptin(filetype, path, filename, v)

    elif key == "c":
        print("\nc. Sắp xếp list theo chiều giảm dần.")
        reverse = False
        c = sapxep(reverse, v)
        print("\nSắp xếp thành công!")

    elif key == "d":
        print("\nd. Lưu list ở câu (c) vào tập tin văn bản.")
        filetype = "vanban"
        path = input("Nhập đường dẫn lưu tập tin: ")
        filename = input("Nhập tên tập tin: ")
        luu_taptin(filetype, path, filename, c)

    elif key == "e":
        print("\ne. Tìm kiếm số n trong list ở câu (d).")
        n = float(input("Nhập số n: "))
        timkiem(n, c)

    elif key == "f":
        print("Bạn đã thoát chương trình.")
        break
    else:
        print("Vui lòng nhập lại.")

