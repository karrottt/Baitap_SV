from p2c1_ham import *
#Tao vector x
print("\nTạo vector x.")
x = np.array([3, 19, 10])
print(x)
#Tao ma tran A, B
print("\nTạo ma trận A.")
A = tao_matran(0, 10, 15, (3, 5))
print("\nTạo ma trận B.")
B = tao_matran(0, 10, 15, (3, 5))
while True:
    print("\n****************CHƯƠNG TRÌNH CHÍNH****************")
    print("**  a. Tính tích x*A.                           **")
    print("**  b. Tính A**0 * B.                           **")
    print("**  c. Tính A**T * B.                           **")
    print("**  d. Thoát.                                   **")
    print("**************************************************")
    key = input("Nhập tùy chọn: ")
    if key == "a":
        #Tich vo huong x*A
        print("\na. Tính tích x*a.")
        tinh_tich(A, x)
    elif key == "b":
        #Phap nhan hadamard A0*B
        print("\nb. Tính A**0 * B.")
        hadamard(A, B)
    elif key == "c":
        #Phep nhan ma tran chuyen vi A va ma tran B
        print("\nc. Tính A**T * B.")
        nhan_chuyenvi(A, B)
    elif key == "d":
        print("Bạn đã thoát chương trình.")
        break
    else:
        print("Vui lòng nhập lại.")


