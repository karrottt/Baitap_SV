from sympy import *
x, y, z = symbols('x y z')

def pt_nhieuan(a1, b1, c1, vp1, a2, b2, c2, vp2, a3, b3, c3, vp3):
    eq1 = Eq(a1 * x + b1 * y + c1 * z, vp1)
    eq2 = Eq(a2 * x + b2 * y + c2 * z, vp2)
    eq3 = Eq(a3 * x + b3 * y + c3 * z, vp3)
    answer = solve((eq1, eq2, eq3), (x, y, z))
    print("\nKet qua cua he phuong trinh la: %s." %answer)
    return answer

#tinh gioi han
def gioihan(f, x0):
    answer = limit(f, x, x0)
    print("\nKet qua gioi han: %s." %answer)
    return answer

#tinh dao ham
def daoham(f):
    answer = diff(f, x)
    print("\nDao ham cua %s la: %s." %(f, answer))
    return answer

#tinh nguyen ham
def nguyenham(f):
    answer = integrate(f, x)
    print("\nNguyen ham cua %s la %s." %(f, answer))

#tinh tich phan
def tichphan(f, gh1, gh2):
    answer = integrate(f, (x, gh1, gh2))
    print("\nTich phan cua [%s] chay tu [%s] den [%s] la: [%s]." %(f, gh1, gh2, answer))
    return answer
