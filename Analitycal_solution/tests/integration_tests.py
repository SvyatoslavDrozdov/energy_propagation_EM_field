from Analitycal_solution.core.sp_integration import sphere_integration
import numpy as np
from scipy.integrate import quad

pi = np.pi
radius = 2.23


def constant_func(x, y, z):
    return 1


def test_function_1(x, y, z):
    return x ** 2 + y ** 2


def test_function_2(x, y, z):
    return (x * y * z) ** 2


def test_function_3(x, y, z):
    return ((x + 2) * (y - 3.4) * (z + 4)) ** 2


test_answer_1 = 8 * pi * radius ** 4 / 3
test_answer_2 = 4 * pi * radius ** 8 / 105
test_answer_3 = 4 * pi * radius ** 8 / 105

zero_position = [0, 0, 0]
some_position = [-2, 3.4, -4]

sphere_surface_area = sphere_integration(constant_func, radius, zero_position)
sphere_surface_area_def = 4 * pi * radius ** 2

print(f'sphere_surface_area = {sphere_surface_area}')
print(f'sphere_surface_area_def = {sphere_surface_area_def}\n')

print(f'test_function_1 = {sphere_integration(test_function_1, radius, zero_position)}')
print(f'test_answer_1 = {test_answer_1}\n')

print(f'test_function_2 = {sphere_integration(test_function_2, radius, zero_position)}')
print(f'test_answer_2 = {test_answer_2}\n')

print(f'test_function_3 = {sphere_integration(test_function_3, radius, some_position)}')
print(f'test_answer_3 = {test_answer_2}')
