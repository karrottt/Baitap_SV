from sympy import *
x, y, z = symbols('x y z')

def pt_nhieuan(a1, b1, c1, vp1, a2, b2, c2, vp2, a3, b3, c3, vp3):
    eq1 = Eq(a1 * x + b1 * y + c1 * z, vp1)
    eq2 = Eq(a2 * x + b2 * y + c2 * z, vp2)
    eq3 = Eq(a3 * x + b3 * y + c3 * z, vp3)
    answer = solve((eq1, eq2, eq3), (x, y, z))
    print("\nKết quả của hệ phương trình: %s." %answer)
    return answer

#tinh gioi han
def gioihan(f, x0):
    answer = limit(f, x, x0)
    print("\nKết quả của giới hạn: %s." %answer)
    return answer

#tinh dao ham
def daoham(f):
    answer = diff(f, x)
    print("\nĐạo hàm của %s là: %s." %(f, answer))
    return answer

#tinh nguyen ham
def nguyenham(f):
    answer = integrate(f, x)
    print("\nNguyên hàm của %s là %s." %(f, answer))

#tinh tich phan
def tichphan(f, gh1, gh2):
    answer = integrate(f, (x, gh1, gh2))
    print("\nTích phân của [%s] chạy từ [%s] đến [%s] là:\n [%s]." %(f, gh1, gh2, answer))
    return answer
