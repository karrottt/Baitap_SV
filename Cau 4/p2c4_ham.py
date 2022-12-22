from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np


def cb_dulieu(start, stop, num):
    dl = np.linspace(start, stop, num)
    return dl


def yenngua():
    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)
    x, y = np.meshgrid(x, y)
    z = (x / 3) ** 2 - (y / 2) ** 2
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    #Vẽ mặt Rosenbrock
    rosen_surf = ax.plot_surface(x, y, z, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    #Thiết lập tham số cho trục z
    ax.set_zlim(-5, 5)
    # Thiết lập màu dựa trên giá trị của hàm.
    fig.colorbar(rosen_surf, shrink=0.5, aspect=5)
    #Hiển thị hình
    plt.show()

def hyperbolic():
    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)
    x, y = np.meshgrid(x, y)
    z = (((x/3)**2 + (y/5)**2 - 1)**(1/2))*2
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    #Vẽ mặt Rosenbrock
    rosen_surf = ax.plot_surface(x, y, z, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    #Thiết lập tham số cho trục z
    ax.set_zlim(-5, 5)
    # Thiết lập màu dựa trên giá trị của hàm.
    fig.colorbar(rosen_surf, shrink=0.5, aspect=5)
    #Hiển thị hình
    plt.show()

def matcau():
    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)
    x, y = np.meshgrid(x, y)
    z = (4 - (x+2)**2 - (y-1)**2)**(1/2) + 4
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    #Vẽ mặt Rosenbrock
    rosen_surf = ax.plot_surface(x, y, z, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    #Thiết lập tham số cho trục z
    ax.set_zlim(-5, 5)
    # Thiết lập màu dựa trên giá trị của hàm.
    fig.colorbar(rosen_surf, shrink=0.5, aspect=5)
    #Hiển thị hình
    plt.show()


