import numpy as np
np.random.seed(123)

def tao_matran(low, high, size, mn):
    A = np.random.randint(low, high, size).reshape(mn)
    print("Ma trận có kích thước %s là: \n%s." %(mn, A))
    return A

def tinh_tich(x, A):
    answer = np.dot(A, x)
    print("Tích của ma trận A với đại lượng vô hướng x là: \n%s." %answer)
    return answer

def hadamard(A, B):
    answer = np.multiply(A, B)
    print("Phép nhân hadamard hai ma trận A và B là: \n%s." %answer)
    return answer

def nhan_chuyenvi(A, B):
    A_chuyenvi = A.T
    answer = np.dot(A_chuyenvi, B)
    print("Phép nhân ma trận chuyển vị A và ma trận B là: /n", answer)
    return answer

