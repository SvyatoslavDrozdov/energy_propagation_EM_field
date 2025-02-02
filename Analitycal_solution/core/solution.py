import numpy as np
from Analitycal_solution.core.sp_integration import sphere_integration

pi = np.pi
c = 1


def get_solution(u_0, du_dt_0):
    """
    This function implements calculation of the analytical solution of the differential equation
            u_xx + u_yy + u_zz - c^(-2) u_tt = 0
    :param u_0: initial value of function u(x,y,z,t=0)
    :param du_dt_0: initial value of derivative du/dt(x,y,z,t=0)
    :return: real function u(x,y,z,t)
    """

    def df_dt(func, time):
        dt = 1e-10
        return (func(time + dt / 2) - func(time - dt / 2)) / dt

    def solution(x, y, z, t):
        center_of_the_sphere = [x, y, z]

        first_term = sphere_integration(du_dt_0, c * t, center_of_the_sphere)
        first_term /= 4 * pi * c ** 2 * t

        def sub_second_term(time):
            return sphere_integration(u_0, c * time, center_of_the_sphere) / time

        second_term = df_dt(sub_second_term, t)
        second_term /= 4 * pi * c ** 2

        return first_term + second_term

    return solution

