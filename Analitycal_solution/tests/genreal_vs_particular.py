import numpy as np
from Analitycal_solution.core.solution import get_solution
from Analitycal_solution.core.particular_solution import get_particular_solution
import matplotlib.pyplot as plt
import time


def u_0(x, y, z):
    k = 10
    return np.e ** (-x ** 2 - y ** 2 - z ** 2) * np.cos(k * z)


def du_dt_0(x, y, z):
    return 0


u_general = get_solution(u_0, du_dt_0)
u_particular = get_particular_solution()

x_0 = 0.95
y_0 = 1.1
z_0 = 4
time_moment = 3

print(f'u_0 = {u_0(x_0, y_0, z_0)}')
print(f'u_general = {u_general(x_0, y_0, z_0, time_moment)}')
print(f'u_particular = {u_particular(x_0, y_0, z_0, time_moment)}')

get_plot = False
if get_plot:
    TIME = np.linspace(0.01, 5, 50)
    general_solution = []
    particular_solution = []
    for t in TIME:
        general_solution.append(u_general(x_0, y_0, z_0, t))
        particular_solution.append(u_particular(x_0, y_0, z_0, t))

    plt.plot(TIME, general_solution, label='general solution')
    plt.plot(TIME, particular_solution, label='particular solution')
    plt.legend()
    plt.show()

number_of_points = int(1e3)
print('\n')

general_solution_time = time.time()
for i in range(number_of_points):
    u_general(x_0, y_0, z_0, time_moment)
print(f'Time to get general solution: {time.time() - general_solution_time}')

particular_solution_time = time.time()
for i in range(number_of_points):
    u_particular(x_0, y_0, z_0, time_moment)
print(f'Time to get particular solution: {time.time() - particular_solution_time}')
