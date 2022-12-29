import numpy as np
from sympy import *
import matplotlib.pyplot as plt

#ham so y = x**4 - 2*x**2 - 3
def daoham(y, n):
  answer = diff(y, x, n)
  print("\nDao ham bac %s cua ham so y la: %s." %(n, answer))
  return answer

def ham_bac_4 (a, b, c, d, e, x):
  y = a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e
  return y

def ham_bac_3 (b, c, d, e, x):
  y1 = b * x ** 3 + c * x ** 2 + d * x + e
  return y1

def ham_bac_2 (c, d, e, x):
  y2 = c * x ** 2 + d * x + e
  return y2

def ham_bac_1 (d, e, x):
  y3 = d * x + e
  return y3

def sinh_dulieu (start, stop, num):
  x = np.linspace(start, stop, num)
  return x

x = sinh_dulieu(-10, 10, 50)
y = ham_bac_4(1, 0, -2, 0, -3, x)
y1 = ham_bac_3(4, 0, -4, 0, x)
y2 = ham_bac_2(12, 0, -4, x)
y3 = ham_bac_1(24, 0, x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x, y1)
ax.plot(x, y2)
ax.plot(x, y3)

ax.set_title("Đồ thị phương trình y, y', y'', y'''")
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")


plt.plot(x, y, marker="x", mec='purple', mfc='purple', label="y")
plt.plot(x, y1, marker=".", mec='brown', mfc='brown', label="y'")
plt.plot(x, y2, marker="*", mec='pink', mfc='pink',label="y''")
plt.plot(x, y3, marker="+", mec='y', mfc='y',label="y'''")


ax.legend()
plt.show()