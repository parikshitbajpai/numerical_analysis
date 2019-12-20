import math
import scipy
import scipy.linalg

def f(x):                                                    # First test function: two equations
    y = scipy.zeros((2,1))                                   # Initialize output vector
    y[0] = 2.0 * math.exp(x[0]*x[1]) -2.0*x[0] +2.0*x[1] -2  # Assign function values
    y[1] = x[0]**5 + x[0]* x[1]**5 -2.0*x[1]
    return y

def Df(x):                                                   # Jacobian for first test case
    J = scipy.zeros((2,2))                                   # Initialize as 2-by-2 array
    J[0,0] = 2.0 * x[1] * math.exp(x[0]*x[1]) - 2.0          # Assign values
    J[0,1] = 2.0 * x[0] * math.exp(x[0]*x[1]) + 2.0
    J[1,0] = 5.0 * x[0]**4 + x[1]**5
    J[1,1] = 5.0 * x[0] * x[1]**4 - 2.0
    return J

def fN(x,N,l):                                               # Second test function with parameter l and n equations
    y = scipy.zeros((N,1))                                   # Initialize output vector
    for i in range(0,N-1):                                   # Assign function values in loop
        y[i] = x[i] - math.exp(l * math.cos((i+1.0)*scipy.sum(x)))
    return y

def DfN(x,N,l):                                              # Jacobian for second test case
    J = scipy.identity(N)                                    # Initialize as N-by-N array
    S = sum(x)                                               # Compute sum
    for i in range(0,N):                                     # Assign values
        J[i,:] = J[i,:] + (i+1.0) * l * math.sin((i+1.0)*S) * math.exp(l * math.cos((i+1.0)*S)) * scipy.ones((1,N))
    return J

    
