import numpy as np
from Analitycal_solution.core.solution import get_solution
from Analitycal_solution.plotting.plotting import plot_field


def u_0(x, y, z):
    # return np.e ** (-x ** 2 - y ** 2) / (z ** 10 + 1)
    k = 10
    return np.e ** (-x ** 2 - y ** 2 - z ** 2) * np.cos(k * z)
    # return np.cos(k * z)


def du_dt_0(x, y, z):
    return 0


u = get_solution(u_0, du_dt_0)


def u_t(x, y, z):
    t = 6
    return u(x, y, z, t)


a_calculate = -10
b_calculate = 10
xlim_calculate = [a_calculate, b_calculate]
ylim_calculate = [a_calculate, b_calculate]
zlim_calculate = [a_calculate, b_calculate]
limits_to_calculate = [xlim_calculate, ylim_calculate, zlim_calculate]

a_show = -8
b_show = 8
xlim_show = [a_show, b_show]
ylim_show = [a_show, b_show]
zlim_show = [a_show, b_show]
limits_to_show = [xlim_show, ylim_show, zlim_show]

point_num = 16
threshold = 1e-5
geometry = [limits_to_calculate, limits_to_show, point_num, threshold]

plot_field(geometry, u_t)
