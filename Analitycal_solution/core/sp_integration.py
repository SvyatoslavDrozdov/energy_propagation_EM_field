import numpy as np
from scipy.integrate import quad

pi = np.pi


def spherical_function(decart_function, center_of_decart_system):
    """
    This function change arguments of f(x,y,z) from cartesian coordinate system to a spherical coordinate system with
    the origin in the point 'center_of_decart_system' f(rho, theta, phi)
    :param decart_function: f(x,y,z)
    :param center_of_decart_system: [x_origin, y_origin, z_origin]
    :return:
    """
    def inner_function(rho, theta, phi):
        x = center_of_decart_system[0] + rho * np.sin(theta) * np.cos(phi)
        y = center_of_decart_system[1] + rho * np.sin(theta) * np.sin(phi)
        z = center_of_decart_system[2] + rho * np.cos(theta)
        return decart_function(x, y, z)

    return inner_function


def sphere_integration(func, radius, position):
    """
    This function implements integration over the sphere of a radius 'radius'.
    :param func: integrand function in decart coordinate system: func = func(x,y,z)
    :param radius: radius of the integration sphere
    :param position: the position of the center of sphere: [x,y,z]
    :return: real number
    """
    func = spherical_function(func, position)

    def inner_integral(phi):
        def inner_func(theta):
            return func(radius, theta, phi) * np.sin(theta)

        return quad(inner_func, 0, pi)[0]

    sphere_integral = radius ** 2 * quad(inner_integral, 0, 2 * pi)[0]
    return sphere_integral
