import numpy as np
import matplotlib.pyplot as plt
from math import factorial as fac



def zern_rad(m, n, rho):
    """
    Calculate the radial component of Zernike polynomial (m, n)
    given a grid of radial coordinates rho.

    >>> zernike_rad(3, 3, 0.333)
    0.036926037000000009
    >>> zernike_rad(1, 3, 0.333)
    -0.55522188900000002
    >>> zernike_rad(3, 5, 0.12345)
    -0.007382104685237683
    """

    if (n < 0 or m < 0 or abs(m) > n):
        raise ValueError

    if ((n - m) % 2):
        return rho * 0.0

    pre_fac = lambda k: (-1.0) ** k * fac(n - k) / (fac(k) * fac((n + m) / 2.0 - k) * fac((n - m) / 2.0 - k))

    return sum(pre_fac(k) * rho ** (n - 2.0 * k) for k in range(int((n - m) / 2 + 1)))


def zern(m, n, rho, phi):
    """
    Calculate Zernike polynomial (m, n) given a grid of radial
    coordinates rho and azimuthal coordinates phi.

    >>> zernike(3,5, 0.12345, 1.0)
    0.0073082282475042991
    >>> zernike(1, 3, 0.333, 5.0)
    -0.15749545445076085
    """
    if (m > 0): return zern_rad(m, n, rho) * np.cos(m * phi)
    if (m < 0): return zern_rad(-m, n, rho) * np.sin(-m * phi)
    return zern_rad(0, n, rho)


