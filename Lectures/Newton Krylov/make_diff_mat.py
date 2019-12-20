# Creates first and second order finite difference differentiation matrices on a regular grid with N interior points.
# By L. van Veen, 2019 OnTechU. 
import numpy as np

def D1(x0,x1,N):
    h = (x1 - x0) / float(N+1)
    D = np.zeros((N,N))
    D[0,1] = 1.0
    for i in range(1,N-1):
        D[i,i-1] = -1.0
        D[i,i+1] =  1.0
    D[N-1,N-2] = -1.0
    D = D/(2.0 * h)
    return D

def D2(x0,x1,N):
    h = (x1 - x0) / float(N+1)
    D = np.zeros((N,N))
    D[0,0] = -2.0
    D[0,1] = 1.0
    for i in range(1,N-1):
        D[i,i-1] =  1.0
        D[i,i] = -2.0
        D[i,i+1] =  1.0
    D[N-1,N-2] = 1.0
    D[N-1,N-1] = -2.0
    D = D/(h**2)
    return D
