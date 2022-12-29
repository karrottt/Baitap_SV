from p2c4_ham import *

while True:
    print("*****************************CHUONG TRINH CHINH*****************************")
    print("**  a. Ve do thi mat yen ngua (x/3)**2− (y/2)**2= z.                      **")
    print("**  b. Ve do thi mat hyperbolic 1 tang (x/3)**2+ (y/5)**2− (z/2)**2= 1    **")
    print("**  c. Ve do thi mat cau (x + 2)**2 + (y − 1)**2 + (z − 4)**2 = 4         **")
    print("**  d. Thoat                                                              **")
    print("****************************************************************************")
    key = input("Nhap tuy chon: ")
    if key == "a":
        dt_yenngua()
    elif key == "b":
        dt_hyperbolic()
    elif key == "c":
        dt_matcau()
    elif key == "d":
        print("Ban da thoat chuong trinh.")
        break
    else:
        print("Vui long nhap lai.")
