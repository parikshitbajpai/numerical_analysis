# Compute the exact solution for the BVP u u' - nu u'' = 0, u(0)=L, u(1)=R. NOTE: there is a pole at x=-B/A. 
# If the pole is inside [x0,x1] a warning is printed and 0 is returned. By L van Veen, OnTechU, 2019.
import numpy as np

def exact(x,x0,x1,A,B,nu):
    pole = -B/A
    if pole < x0 or pole > x1:
        F = -2.0 * nu * A / np.tanh(A*x +B)
    else:
        print('Warning: singular solution, pole at %f.' % (pole))
        F = 0.0
    return F
