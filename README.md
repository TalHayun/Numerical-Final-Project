        
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
Integrate the function f in the closed range [a,b] using at most n points.
Your main objective is minimizing the integration error.
Your secondary objective is minimizing the running time.
The assignment will be tested on variety of different functions.
Integration error will be measured compared to the actual value of the definite integral.
It is forbidden to call f more than n times.

