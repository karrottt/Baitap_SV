from p2c4_ham import *

while True:
    print("\n***************CHƯƠNG TRÌNH CHÍNH***************")
    print("**  a. Vẽ đồ thị mặt yên ngựa.                **")
    print("**  b. Vẽ đồ thị mặt hyperbolic một tầng.     **")
    print("**  c. Vẽ đồ thị mặt cầu                      **")
    print("**  d. Thoát.                                 **")
    print("************************************************")
    key = input("Nhập tùy chọn: ")
    if key == "a":
        dt_yenngua()
    elif key == "b":
        dt_hyperbolic()
    elif key == "c":
        dt_matcau()
    elif key == "d":
        print("Bạn đã thoát chương trình.")
        break
    else:
        print("Vui lòng nhập lại.")
