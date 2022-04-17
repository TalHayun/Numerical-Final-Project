"""
In this assignment you should interpolate the given function.
"""

import numpy as np
import matplotlib.pyplot as plt
import timeit
import math
import random
import matplotlib


class Assignment1:
    def __init__( self ):
        """
        Here goes any one time calculation that need to be made before
        starting to interpolate arbitrary functions.
        """

        pass

    def get_cubic(self, a, b, c, d ):
        return lambda t: np.power(1 - t, 3) * a + 3 * np.power(1 - t, 2) \
                         * t * b + 3 * (1 - t) * np.power(t, 2) * c + np.power(t, 3) * d

    def get_bezier_cubic(self, A, B, points ):
        return [self.get_cubic(points[i], A[i], B[i], points[i + 1])
                for i in range(len(points) - 1)]

    def interpolate( self, f: callable, a: float, b: float, n: int ) -> callable:
        """
        
        Parameters
        ----------
        f : callable. it is the given function
        a : float
            beginning of the interpolation range.
        b : float
            end of the interpolation range.
        n : int
            maximal number of points to use.

        Returns
        -------
        The interpolating function.
        """
        d = Assignment1()
        # Find union points in function
        x_cp, y_cp = [], []
        for i in range(n - 1):
            x_cp.append(a + ((b - a) * i / (n - 1)))
            y_cp.append(f(x_cp[i]))
        x_cp.append(b)
        y_cp.append(f(b))

        # Only one point to use
        if n == 1:
            return f((a + b) / 2)

        # C - coefficients matrix
        C = 4 * np.identity(n - 1)
        np.fill_diagonal(C[1:], 1)
        np.fill_diagonal(C[:, 1:], 1)
        C[0, 0], C[n - 2, n - 2], C[n - 2, n - 3] = 2, 7, 2

        # P - points vector
        P_x, P_y = [], []
        for i in range(n - 1):
            if i == 0:
                P_x.append(x_cp[i] + 2 * x_cp[i + 1])
                P_y.append(y_cp[i] + 2 * y_cp[i + 1])
            elif i == n - 2:
                P_x.append(8 * x_cp[i] + x_cp[i + 1])
                P_y.append(8 * y_cp[i] + y_cp[i + 1])
            else:
                P_x.append(4 * x_cp[i] + 2 * x_cp[i + 1])
                P_y.append(4 * y_cp[i] + 2 * y_cp[i + 1])

        # solve system, find Xa & Xb
        A_x = np.linalg.solve(C, P_x)
        B_x = [0] * (n - 1)
        for i in range(n - 2):
            B_x[i] = 2 * x_cp[i + 1] - A_x[i + 1]
        B_x[n - 2] = (A_x[n - 2] + x_cp[n - 1]) / 2

        # solve system, find Ya & Yb
        A_y = np.linalg.solve(C, P_y)
        B_y = [0] * (n - 1)
        for i in range(n - 2):
            B_y[i] = 2 * y_cp[i + 1] - A_y[i + 1]
        B_y[n - 2] = (A_y[n - 2] + y_cp[n - 1]) / 2

        # Combine the X&Y to point argument
        A, B, Points = [], [], []
        for i in range(n-1):
            A.append((A_x[i], A_y[i]))
            B.append((B_x[i], B_y[i]))
            Points.append((x_cp[i], y_cp[i]))
        Points.append((x_cp[n-1], y_cp[n-1]))

        # convert the array to np.array
        Points, A, B = np.array(Points), np.array(A), np.array(B)

        # find curves by the points and control points
        curves = self.get_bezier_cubic(A, B, Points)
        # union each polynomial in curve by t
        return lambda x: curves[math.floor(((x - a) / (b - a))*(n - 1))]((((x - a) / (b - a))*(n - 1)) % 1)[1] \
            if a <= x < b else curves[n - 1]((((x - a) / (b - a)) * (n - 1)) % 1)[1]


##########################################################################


import unittest
from functionUtils import *
from tqdm import tqdm


class TestAssignment1(unittest.TestCase):

    def test_with_poly( self ):
        T = time.time()

        ass1 = Assignment1()
        mean_err = 0

        d = 30
        for i in tqdm(range(100)):
            a = np.random.randn(d)

            f = np.poly1d(a)

            ff = ass1.interpolate(f, -10, 10, 100)

            xs = np.random.random(200)
            err = 0
            for x in xs:
                yy = ff(x)
                y = f(x)
                err += abs(y - yy)

            err = err / 200
            mean_err += err
        mean_err = mean_err / 100

        T = time.time() - T
        print(T)
        print(mean_err)

    def test_with_poly_restrict( self ):
        ass1 = Assignment1()
        a = np.random.randn(5)
        f = RESTRICT_INVOCATIONS(10)(np.poly1d(a))
        ff = ass1.interpolate(f, -10, 10, 10)
        xs = np.random.random(20)
        for x in xs:
            yy = ff(x)


if __name__ == "__main__":
    unittest.main()
