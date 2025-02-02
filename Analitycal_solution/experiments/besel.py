import numpy as np
import scipy.special as sp
from scipy.integrate import quad
import time

pi = np.pi
# Функция Бесселя первого рода J_n(x)
x = 2.43
I_0 = sp.iv(0, x)

A = 2
B = -4


def Acos_Bsin(phi):
    return np.exp(A * np.cos(phi) + B * np.sin(phi))


calculation_number = int(1e2)

time_def = time.time()

I_def_array = []
for i in range(calculation_number):
    I_def_array.append(quad(Acos_Bsin, 0, 2 * pi)[0])
print(f'time_def = {time.time() - time_def}')

time_bessel = time.time()
I_bessel_array = []
for i in range(calculation_number):
    I_bessel_array.append(2 * pi * sp.iv(0, (A ** 2 + B ** 2) ** 0.5))
print(f'time_bessel = {time.time() - time_bessel}\n')

I_def = quad(Acos_Bsin, 0, 2 * pi)[0]
I_bessel = 2 * pi * sp.iv(0, (A ** 2 + B ** 2) ** 0.5)
print(f'I_def = {I_def}')
print(f'I_bessel = {I_bessel}')

# The difference is about 140 time
x = 650
print(sp.iv(0, x) * np.exp(-x/10))
