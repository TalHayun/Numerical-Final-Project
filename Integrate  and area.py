"""
In this assignment you should find the area enclosed between the two given functions.
The rightmost and the leftmost x values for the integration are the rightmost and
the leftmost intersection points of the two functions.

The functions for the numeric answers are specified in MOODLE.


This assignment is more complicated than Assignment1 and Assignment2 because:
    1. You should work with float32 precision only (in all calculations) and minimize the floating point errors.
    2. You have the freedom to choose how to calculate the area between the two functions.
    3. The functions may intersect multiple times. Here is an example:
        https://www.wolframalpha.com/input/?i=area+between+the+curves+y%3D1-2x%5E2%2Bx%5E3+and+y%3Dx
    4. Some of the functions are hard to integrate accurately.
       You should explain why in one of the theoretical questions in MOODLE.

"""

import numpy as np
import time
import random
from assignment2 import Assignment2


class Assignment3:
    def __init__( self ):
        """
        Here goes any one time calculation that need to be made before
        solving the assignment for specific functions.
        """

        pass

    def integrate( self, f: callable, a: float, b: float, n: int ) -> np.float32:
        """
        Integrate the function f in the closed range [a,b] using at most n
        points. Your main objective is minimizing the integration error.
        Your secondary objective is minimizing the running time. The assignment
        will be tested on variety of different functions.

        Integration error will be measured compared to the actual value of the
        definite integral.

        Note: It is forbidden to call f more than n times.

        Parameters
        ----------
        f : callable. it is the given function
        a : float
            beginning of the integration range.
        b : float
            end of the integration range.
        n : int
            maximal number of points to use.

        Returns
        -------
        np.float32
            The definite integral of f between a and b
        """
        n -= 1
        if n % 2 == 1: # check n points is even or odd
            n -= 1 # decrease by 1
        h = (b - a) / n # define the amount of intervals
        f0, f1 = f(a) + f(b), 0
        for i in range(1, n): # loop for through the intervals
            x = a + i * h # interval's left border
            tmp = f(x)

            if i % 2 == 0: # there is an even interval
                f0 += 2 * tmp
            else: # there is an odd interval
                f1 += tmp
        return np.float32(((h / 3) * (f0 + 4 * f1))) # calculate integration by simpson's rule formula


    def areabetween( self, f1: callable, f2: callable ) -> np.float32:
        """
        Finds the area enclosed between two functions. This method finds
        all intersection points between the two functions to work correctly.

        Example: https://www.wolframalpha.com/input/?i=area+between+the+curves+y%3D1-2x%5E2%2Bx%5E3+and+y%3Dx

        Note, there is no such thing as negative area.

        In order to find the enclosed area the given functions must intersect
        in at least two points. If the functions do not intersect or intersect
        in less than two points this function returns NaN.
        This function may not work correctly if there is infinite number of
        intersection points.
`

        Parameters
        ----------
        f1,f2 : callable. These are the given functions

        Returns
        -------
        np.float32
            The area between function and the X axis

        """

        # replace this line with your solution
        ass2, ass3, result = Assignment2(), Assignment3(), 0
        inter_points = (ass2.intersections(f1, f2, 1, 100, 0.00001))  # find the intersect points of the functions and sort them
        f = lambda x: f1(x) - f2(x)
        if len(inter_points) < 2: # there are not inter points of the functions
            return None
        else:
            inter_points = sorted(inter_points) # sorted the inter points for integration between adjacent points
            for i in range(0, len(inter_points) - 1):
                result += abs(ass3.integrate(f, inter_points[i], inter_points[i + 1], 400)) # adding to result the integration area between adjacent points
            return np.float32(result)



##########################################################################
from numpy import sin
import unittest
from sampleFunctions import *
from tqdm import tqdm

class TestAssignment3(unittest.TestCase):

    def test_integrate_float32( self ):
        ass3 = Assignment3()
        f1 = np.poly1d([-1, 0, 1])
        r = ass3.integrate(f1, -1, 1, 10)
        self.assertEqual(r.dtype, np.float32)

if __name__ == "__main__":
    unittest.main()
