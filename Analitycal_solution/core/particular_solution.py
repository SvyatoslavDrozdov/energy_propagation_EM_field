import numpy as np
from scipy.integrate import quad
import scipy.special as sp

pi = np.pi
c = 1
sigma = 1
k = 10


def get_particular_solution():
    """
    This function implements calculation of one particular analytical solution.
    """

    def df_dt(func, time):
        dt = 1e-10
        return (func(time + dt / 2) - func(time - dt / 2)) / dt

    def solution(x, y, z, t):
        r_0 = (x ** 2 + y ** 2 + z ** 2) ** 0.5

        def under_derivative(time):
            R = c * time

            def psi(theta):
                multiplier_1 = np.exp(-2 * R * z / sigma ** 2 * np.cos(theta))
                multiplier_2 = sp.iv(0, 2 * R / sigma ** 2 * (x ** 2 + y ** 2) ** 0.5 * np.sin(theta))
                multiplier_3 = np.cos(k * (z + R * np.cos(theta)))
                multiplier_4 = np.sin(theta)
                return multiplier_1 * multiplier_2 * multiplier_3 * multiplier_4

            I = quad(psi, 0, pi)[0]
            I *= 2 * pi * R ** 2 * np.exp(-(r_0 ** 2 + R ** 2) / sigma ** 2)
            I /= time
            return I

        u = df_dt(under_derivative, t)
        u /= 4 * pi * c ** 2
        return u

    return solution
