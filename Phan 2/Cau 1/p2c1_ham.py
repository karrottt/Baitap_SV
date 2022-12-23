import numpy as np
np.random.seed(123)

def tao_matran(low, high, size, mn):
    A = np.random.randint(low, high, size).reshape(mn)
    print("Ma tran co kich thuoc %s la: \n%s" %(mn, A))
    return A

def tich_vohuong(x, A):
    answer = np.dot(A, x)
    print("Tich cua ma tran A voi dai luong vo huong x la: \n%s" %answer)
    return answer

def hadamard(A, B):
    answer = np.multiply(A, B)
    print("Phep nhan hadamard 2 ma tran A va B la: \n%s" %answer)
    return answer

def nhan_chuyenvi(A, B):
    A_chuyenvi = A.T
    answer = np.dot(A_chuyenvi, B)
    print("Phep nhan ma tran chuyen vi A va ma tran B la:", answer)
    return answer

