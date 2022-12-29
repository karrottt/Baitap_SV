from p2c1_ham import *
#Tao vector x
print("\nTao vector x.")
x = np.array([3, 19, 10])
print(x)
#Tao ma tran A, B
print("\nTao ma tran A.")
A = tao_matran(0, 10, 15, (3, 5))
print("\nTao ma tran B.")
B = tao_matran(0, 10, 15, (3, 5))
while True:
    print("\n****************CHUONG TRINH CHINH****************")
    print("**  a. Tinh tich x*a.                           **")
    print("**  b. Tinh A**0 * B.                           **")
    print("**  c. Tinh A**T * B.                           **")
    print("**  d. Thoat                                    **")
    print("**************************************************")
    key = input("Nhap tuy chon: ")
    if key == "a":
        #Tich vo huong x*A
        print("\na - Tinh tich vo huong x*A.")
        tinh_tich(A, x)
    elif key == "b":
        #Phap nhan hadamard A0*B
        print("\nb - Phep nhan hadamard.")
        hadamard(A, B)
    elif key == "c":
        #Phep nhan ma tran chuyen vi A va ma tran B
        print("\nc - Phep nhan ma tran chuyen vi A va ma tran B.")
        nhan_chuyenvi(A, B)
    elif key == "d":
        print("Ban da thoat chuong trinh.")
        break
    else:
        print("Vui long nhap lai.")


