## Numerical Analysis Assignment 2
## Date: 8 November 2019
## This file defines parameters and call Newton's method for both linear and rational approximations
## Authors: Marcos Machado, Parikshit Bajpai

import numpy as np
from newton_1 import newton
from newton_2 import modified_newton
from compute import compute_A
from compute import compute_B

## Parameters initialization
M = 5                                                      ## This is the number of terms in the somation function
delta = 0                                                  ## Delta initialization
a = np.zeros(M)                                            ## Zeros arrays initialization
b = np.zeros(M)
a = [1.0,1.0,1.0,1.0,1.0]                                  ## Define a and b for fabricated solutions, number of entries is M, defined above
b = [1.0,1.0,1.0,1.0,1.0]
a = np.array(a)**2                                         ## Define a and b for fabricated solutions, number of entries is M, defined above
b = np.array(b)**2                                         ## a and b inserted here is suppose to be squared
eps_f = 1e-8                                               ## Error
eps_x = 1e-8                                               ## Tolerance
N = 100                                                    ## Number of iterations in the Newton's method
x0 = 0.0                                                   ## Initial guess for solutions

## If random a and b are random
# a = (np.random.normal(0,0.1,M))**2
# b = (np.random.uniform(-1,0,M))**2

# for i in range(M):                                       ## Delta definition
#     delta += a[i]/(b[i]**2.0)
# delta = delta*np.random.uniform(0.1,0.9)
delta = 1.0

## Function and derivative
def f(x):                                                  ## Function definition (a and b is already squared in the array above!!!)
    f = -delta
    for i in range(M):
        f += a[i]/(b[i]+x)**2.0
    return f

def fp(x):                                                 ## Function derivative (a and b is already squared in the array above!!!)
    fp = 0.0
    for i in range(M):
        fp += (-2.0*a[i])/(b[i]+x)**3.0
    return fp

x = newton(f,fp,x0,eps_f,eps_x,N)                          ## Calling Newton's method and all parameters
x = modified_newton(f,fp,x0,eps_f,eps_x,N,delta,a,b,M)     ## Calling Newton's modified method and all parameters
