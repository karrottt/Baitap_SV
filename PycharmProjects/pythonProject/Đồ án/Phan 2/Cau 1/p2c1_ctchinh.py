from p2c1_ham import *

x = float(input("Nhap so x: "))

#Tao ma tran A, B
print("\nTao ma tran A.")
A = tao_matran(0, 10, 15, (3, 5))
print("\nTao ma tran B.")
B = tao_matran(0, 10, 15, (3, 5))

#Tich vo huong x*A
print("\n1 - Tinh tich vo huong x*A.")
tich_vohuong(x, A)

#Phap nhan hadamard A0*B
print("\n2 - Phep nhan hadamard.")
hadamard(A, B)

#Phep nhan ma tran chuyen vi A va ma tran B
print("\n3 - Phep nhan ma tran chuyen vi A va ma tran B.")
nhan_chuyenvi(A, B)