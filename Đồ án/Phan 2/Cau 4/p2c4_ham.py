import numpy as np
import matplotlib.pyplot as plt

def dt_yenngua():
    x = np.linspace(-10, 10, 1000)
    y = np.linspace(-10, 10, 1000)
    x, y = np.meshgrid(x, y)
    z = (x / 3) ** 2 - (y / 2) ** 2
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.set_zlim(-15, 15)
    yenngua = ax.plot_surface(x, y, z, cmap=plt.cm.cool, linewidth=0, antialiased=True)
    fig.colorbar(yenngua, shrink=0.5, aspect=5)
    ax.set_title("Đồ thị mặt yên ngựa: " + r"$\left(\frac{x}{3}\right)^{2} - \left(\frac{y}{2}\right)^{2} = z.$")
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.set_zlabel("Trục cao - z")
    plt.show()

def dt_hyperbolic():
    x = np.linspace(-100, 100, 100)
    y = np.linspace(-100, 100, 100)
    x, y = np.meshgrid(x, y)
    z = (abs((x / 3) ** 2 + (y / 5) ** 2 - 1) ** (1 / 2)) * 2

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    hyperbolic_1tang1 = ax.plot_surface(x, y, z, cmap=plt.cm.spring, linewidth=0, antialiased=True)
    ax.plot_surface(x, y, -z, cmap=plt.cm.spring, linewidth=0, antialiased=True)
    fig.colorbar(hyperbolic_1tang1, shrink=0.5, aspect=5)
    ax.set_title("Đồ thị hyperbolic một tầng: " + r"$\left(\frac{x}{3}\right)^{2} + \left(\frac{y}{5}\right)^{2}  - \left(\frac{z}{2}\right)^{2} = 1.$")
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.set_zlabel("Trục cao - z")
    plt.show()

def dt_matcau():
    # (x - x0)^2 + (y - y0)^2 + (z - z0)^2 = R^2
    # (x + 2)^2 + (y − 1)^2 + (z − 4)^2 = 4
    fig = plt.figure(facecolor="White")
    ax = plt.axes(projection="3d")
    # 0 <= θ <= pi, 0 <= φ <= 2*pi
    # u = θ, v = φ
    u = np.linspace(0, np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)

    r = 2
    x0 = -2
    y0 = 1
    z0 = 4
    # θ: theta
    # x = x0 + r*sin(θ)*cos(φ)
    # y = y0 + r*sin(θ)*sin(φ)
    # z = z0 + r*cos(θ)
    x = x0 + r * np.outer(np.cos(v), np.sin(u))
    y = y0 + r * np.outer(np.sin(v), np.sin(u))
    z = z0 + r * np.outer(np.ones(np.size(v)), np.cos(u))
    ax.set_title("Đồ thị mặt cầu: " + r"$(x + 2)^2 + (y − 1)^2 + (z − 4)^2 = 4$")
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.set_zlabel("Trục cao - z")
    matcau = ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=plt.cm.cool, linewidth=0, antialiased=True)
    fig.colorbar(matcau, shrink=0.5, aspect=5)
    plt.show()