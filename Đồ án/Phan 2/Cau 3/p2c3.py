import numpy as np
import matplotlib.pyplot as plt

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

x = sinh_dulieu(-10, 10, 30)
#ham so y = x**4 - 2*x**2 - 3
y = ham_bac_4(1, 0, -2, 0, -3, x)
y1 = ham_bac_3(4, 0, -4, 0, x)
y2 = ham_bac_2(12, 0, -4, x)
y3 = ham_bac_1(24, 0, x)

fig, ax = plt.subplots()
ax.set_title("Đồ thị phương trình y, y', y'', y'''")
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")

plt.plot(x, y, color = "b", linestyle = "solid", marker="o", ms=6, mec = "r", mfc = "white", label=r"$y = x^{4} - 2x^{2} - 3$")
plt.plot(x, y1, color = "c", linestyle = "solid", marker="s", ms=6, mec="g", mfc="white", label=r"$y' = 4x^{3} - 4x$")
plt.plot(x, y2, color = "g", linestyle = "solid", marker="D", ms=6, mec = "y", mfc = 'w', label=r"$y'' = 12x^{2} - 4$")
plt.plot(x, y3, color = "m", linestyle = "solid", marker=">", ms=6, mec = "purple", mfc="w", label=r"$y''' = 24x$")

ax.legend()
plt.show()