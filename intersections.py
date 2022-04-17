"""
In this assignment you should find the intersection points for two functions.
"""

import numpy as np
import time
import random
from collections.abc import Iterable


class Assignment2:
    def __init__( self ):
        """
        Here goes any one time calculation that need to be made before
        solving the assignment for specific functions.
        """

        pass

    def bisection_rec( self, f, a, b, maxerr, Xs ):
        counter_loop, a_new, b_new = 0, a, b

        while f(a_new) * f(b_new) > 0:  # search new pair points with different sign
            a_new = random.uniform(a, b)  # random point between the range
            b_new = random.uniform(a_new, b)  # random point between [a_new, b]
            counter_loop += 1
            if counter_loop == 1000:  # didn't find a pair with different sign - no root
                return

        mid = (a_new + b_new) / 2
        while abs(f(mid)) > maxerr:  # continue to check the midpoint while the mid points isn't smaller maxerr
            if f(a_new) * f(mid) < 0:
                b_new = mid  # update the right border of the section
            else:
                a_new = mid  # update the left border of the section
            mid = (a_new + b_new) / 2
        Xs.append(mid)  # append the midpoint to the roots list
        self.bisection_rec(f, a, mid - maxerr, maxerr, Xs)  # rec the bisection by left side
        self.bisection_rec(f, mid + maxerr, b, maxerr, Xs)  # rec the bisection by right side
        return

    def intersections( self, f1: callable, f2: callable, a: float, b: float, maxerr=0.001 ) -> Iterable:
        """
        Parameters
        ----------
        f1 : callable
            the first given function
        f2 : callable
            the second given function
        a : float
            beginning of the interpolation range.
        b : float

            end of the interpolation range.
        maxerr : float
            An upper bound on the difference between the
            function values at the approximate intersection points.


        Returns
        -------
        X : iterable of approximate intersection Xs such that for each x in X:
            |f1(x)-f2(x)|<=maxerr.

        """
        f = lambda x: f1(x) - f2(x)
        X = []
        while abs(f(a)) < maxerr and abs(f(b)) < maxerr:  # add a and b to the list roots if the borders are roots
            X.append(a)
            X.append(b)
            a += maxerr
            b -= maxerr
        while abs(f(a)) < maxerr < abs(f(b)):
            X.append(a)
            a += maxerr
        while abs(f(a)) > maxerr > abs(f(b)):
            X.append(b)
            b -= maxerr
        self.bisection_rec(f, a, b, maxerr, X)  # find the roots by bisection_rec method
        return X


##########################################################################


import unittest
from sampleFunctions import *
from tqdm import tqdm


class TestAssignment2(unittest.TestCase):

    def test_sqr( self ):

        ass2 = Assignment2()

        f1 = np.poly1d([-1, 0, 1])
        f2 = np.poly1d([1, 0, -1])

        X = ass2.intersections(f1, f2, -1, 1, maxerr=0.001)

        for x in X:
            self.assertGreaterEqual(0.001, abs(f1(x) - f2(x)))

    def test_poly( self ):

        ass2 = Assignment2()

        f1, f2 = randomIntersectingPolynomials(10)

        X = ass2.intersections(f1, f2, -1, 1, maxerr=0.001)

        for x in X:
            self.assertGreaterEqual(0.001, abs(f1(x) - f2(x)))


if __name__ == "__main__":
    unittest.main()
