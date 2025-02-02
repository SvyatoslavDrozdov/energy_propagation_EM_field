import numpy as np
from Analitycal_solution.plotting.plotting import plot_field

a_calculate = -15
b_calculate = 15
xlim_calculate = [a_calculate, b_calculate]
ylim_calculate = [a_calculate, b_calculate]
zlim_calculate = [2 * a_calculate, 2 * b_calculate]
limits_to_calculate = [xlim_calculate, ylim_calculate, zlim_calculate]

a_show = -20
b_show = 20
xlim_show = [a_show, b_show]
ylim_show = [a_show, b_show]
zlim_show = [a_show, b_show]
limits_to_show = [xlim_show, ylim_show, zlim_show]

point_num = 10
threshold = 1e-10
geometry = [limits_to_calculate, limits_to_show, point_num, threshold]


def f(x, y, z):
    return np.exp(-abs(x) - abs(z))


plot_field(geometry, f)
