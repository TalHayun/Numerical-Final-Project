        
# Assignment 1:        
Interpolate the function f in the closed range [a,b] using at most n points.
Your main objective is minimizing the interpolation error.
Your secondary objective is minimizing the running time.
The assignment will be tested on variety of different functions with large n values.
Interpolation error will be measured as the average absolute error at 2*n random points between a and b.
See test_with_poly() below.
It is forbidden to call f more than n times.
This assignment can be solved trivially with running time O(n^2) or it can be solved with running time of O(n) with some preprocessing.
sometimes you can get very accurate solutions with only few points, significantly less than n.

# Assignment 2:
Find as many intersection points as you can.
The assignment will be tested on functions that have at least two intersection points, one with a positive x and one with a negative x.
This function may not work correctly if there is infinite number of intersection points.

# Assignment3:
## integrate:
Integrate the function f in the closed range [a,b] using at most n points.
Your main objective is minimizing the integration error.
Your secondary objective is minimizing the running time.
The assignment will be tested on variety of different functions.
Integration error will be measured compared to the actual value of the definite integral.
It is forbidden to call f more than n times.

## areabetween:
Finds the area enclosed between two functions. This method finds
all intersection points between the two functions to work correctly.
Example: https://www.wolframalpha.com/input/?i=area+between+the+curves+y%3D1-2x%5E2%2Bx%5E3+and+y%3Dx
Note, there is no such thing as negative area.
In order to find the enclosed area the given functions must intersect in at least two points.
If the functions do not intersect or intersect in less than two points this function returns NaN.
This function may not work correctly if there is infinite number of intersection points.

