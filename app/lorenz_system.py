"""
Document: lorenz_system.py
Function: Module for doing Lorenz system-related calculations which returns three floating
          numbers to be used as a first phase encryption key.
Author: PURA, Joshua Elijah L.
Date Created: September 30, 2025
Date Updated: September 30, 2025
Version: 0.0.1
Imported Libraries:
"""

#Imports

import numpy as np
import pytest
from decimal import Decimal, getcontext

class LorenzSystem:

    """
    Function: __init__
    Description: This function gets triggered when the LorenzSystem object is instantiated.
    Arguments:
        sigma (float): The sigma parameter of the Lorenz system.
        rho (float): The rho parameter of the Lorenz system.
        beta (float): The beta parameter of the Lorenz system.
        time (int): The time parameter of the Lorenz system.
    Returns:
        void: This function does not return anything.
    Raises:
        no error detected yet.
    """
    def __init__(self, x = 1.0, y = 1.0, z = 1.0):
        self.x = x
        self.y = y
        self.z = z
        self.dt = 0.01


    @staticmethod
    def __lorenz(sigma, rho, beta, x = 1.0, y = 1.0, z = 1.0):
        """
        Function: lorenz
        Description: This function returns the differential values of x, y, and z with respect to time t in an array format.
        Arguments:
            sigma (float): The sigma parameter of the Lorenz system.
            rho (float): The rho parameter of the Lorenz system.
            beta (float): The beta parameter of the Lorenz system.
        Returns:
            array: This function returns a numpy array of the solved dx, dy, and dz.
        Raises:
               no error detected yet.
        """
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        return np.array([dx, dy, dz])


    def __runge_kutta(self, sigma, rho, beta, time):
        """
        Function: runge_kutta
        Description: This function process and computes the Lorenz system trajectory using 4th-order Runge-Kutta method.
                     This method numerically integrates the Lorenz differential equations over time, starting from the
                     initial (x, y, z) values.

        Returns:
            array: This function returns a numpy array of the last values processed from xs, ys, and zs.
        Raises:
            no error detected yet.
        """
        # Initiating values and arrays needed
        x, y, z = self.x, self.y, self.z
        dt = self.dt
        xs = np.empty(time + 1, dtype=object)
        ys = np.empty(time + 1, dtype=object)
        zs = np.empty(time + 1, dtype=object)
        xs[0], ys[0], zs[0] = x, y, z
        getcontext().prec = 77

        # For Loop to process the first to fourth order of Runge Kutta
        for i in range(time):
            dx1, dy1, dz1 = LorenzSystem.__lorenz(x, y, z, sigma, rho, beta)
            dx2, dy2, dz2 = LorenzSystem.__lorenz(x + dx1 * dt / 2, y + dy1 * dt / 2, z + dz1 * dt / 2, sigma, rho, beta)
            dx3, dy3, dz3 = LorenzSystem.__lorenz(x + dx2 * dt / 2, y + dy2 * dt / 2, z + dz2 * dt / 2, sigma, rho, beta)
            dx4, dy4, dz4 = LorenzSystem.__lorenz(x + dx3 * dt, y + dy3 * dt, z + dz3 * dt, sigma, rho, beta)

            x += (dt / 6) * (dx1 + 2 * dx2 + 2 * dx3 + dx4)
            y += (dt / 6) * (dy1 + 2 * dy2 + 2 * dy3 + dy4)
            z += (dt / 6) * (dz1 + 2 * dz2 + 2 * dz3 + dz4)

            x_decimal = Decimal(str(x))
            y_decimal = Decimal(str(y))
            z_decimal = Decimal(str(z))

            x_str = str(x_decimal).replace('.','').lstrip('0')
            y_str = str(y_decimal).replace('.','').lstrip('0')
            z_str = str(z_decimal).replace('.','').lstrip('0')

            xs[i + 1] = int(x_str)
            ys[i + 1] = int(y_str)
            zs[i + 1] = int(z_str)
        print(np.array([xs[-1], ys[-1], zs[-1]], dtype=object).tolist())
        return np.array([xs[-1], ys[-1], zs[-1]], dtype=object).tolist()

    def get_key(self, sigma, rho, beta, time):
        if isinstance(sigma, float) and isinstance(rho, float) and isinstance(beta, float) and isinstance(time, int):
           return self.__runge_kutta(sigma, rho, beta, time)
        else:
            raise TypeError("Sigma, Rho and Beta must be floats. Time must be integer.")

