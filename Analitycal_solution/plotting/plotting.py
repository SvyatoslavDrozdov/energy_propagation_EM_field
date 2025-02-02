import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


# def f(x, y, z):
#     return np.exp(-abs(x) - abs(y) - abs(z))  # Пример функции

def plot_field(geometry, f):
    limits_to_calculate = geometry[0]
    limits_to_show = geometry[1]

    xlim_calculate = limits_to_calculate[0]
    ylim_calculate = limits_to_calculate[1]
    zlim_calculate = limits_to_calculate[2]

    xlim_show = limits_to_show[0]
    ylim_show = limits_to_show[1]
    zlim_show = limits_to_show[2]

    point_num = geometry[2]
    threshold = geometry[3]

    X = np.linspace(xlim_calculate[0], xlim_calculate[1], point_num)
    Y = np.linspace(ylim_calculate[0], ylim_calculate[1], point_num)
    Z = np.linspace(zlim_calculate[0], zlim_calculate[1], point_num)
    X_grid, Y_grid, Z_grid = np.meshgrid(X, Y, Z)

    F = np.zeros((point_num, point_num, point_num))
    i = 0
    for x in X:
        j = 0
        for y in Y:
            k = 0
            for z in Z:
                F[j][i][k] = f(x, y, z)
                k += 1
            j += 1
        i += 1

    mask = np.abs(F) >= threshold

    X_filtered = X_grid[mask]
    Y_filtered = Y_grid[mask]
    Z_filtered = Z_grid[mask]
    F_filtered = F[mask]

    F_abs = np.abs(F_filtered)
    # print(F_abs)
    F_max = np.max(F_abs)
    F_normalized = F_abs / F_max

    F_bright = F_normalized ** 10

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    colors = cm.coolwarm(F_bright)

    ax.scatter(X_filtered, Y_filtered, Z_filtered, c=colors.reshape(-1, 4), alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim(xlim_show[0], xlim_show[1])
    ax.set_ylim(ylim_show[0], ylim_show[1])
    ax.set_zlim(zlim_show[0], zlim_show[1])

    ax.set_box_aspect([1, 1, 1])
    plt.show()
