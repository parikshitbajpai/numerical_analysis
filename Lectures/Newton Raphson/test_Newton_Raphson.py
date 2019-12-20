# Test script for Newton-Raphson iteration. Programmed in lecture 12.
import numpy as np
from Newton_Raphson import Newton_Raphson

# Test problem, change as you like.
def f(x):
    f = np.zeros((2,1))
    f[0,0] = x[0]**2+x[1]**2-1.0
    f[1,0] = x[0]/x[1]-1.0
    return f

def fp(x):
    J = np.zeros((2,2))
    J[0,0] = 2.0 * x[0]
    J[0,1] = 2.0 * x[1]
    J[1,0] = 1.0/x[1]
    J[1,1] = -x[0]/x[1]**2
    return J

eps_f = 1e-12
eps_x = 1e-12
N = 15

x0 = np.array([[0.1],[0.1]])

x = Newton_Raphson(f,fp,x0,eps_f,eps_x,N)
print(x)
