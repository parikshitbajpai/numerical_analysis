## Numerical Analysis Assignment 2
## Date: 8 November 2019
## This file implements Newton's method using rational approximation and plots the residuals vs. the number of iterations.
## Authors: Parikshit Bajpai, Marcos Machado

import numpy as np
from copy import copy
import matplotlib.pylab as plt
from compute import compute_A
from compute import compute_B

## Newton's method inputs: function, derivative, initial guess, error and tolerance, number of iterations, delta,
## coefficients (a and b), number of terms in the somation function (M)

def modified_newton(f,fp,x0,eps_f,eps_x,N,delta,a,b,M):
    flag = 0
    residual = np.zeros((N,2))
    x = copy(x0)
    for i in range(N):
        residual[i,0] = i
        r = f(x)
        residual[i,1] = compute_A(x,M,a,b)/delta - compute_B(x,M,a,b) - x
        x += residual[i,1]
        print('newton2 %d %e %e %e' % (residual[i,0],r,residual[i,1],x))
        if abs(r) < eps_f and abs(residual[i,1]) < eps_x:
            flag = 1
            break
    if flag==1:
        plt.semilogy(residual[:,0],np.absolute(residual[:,1]),'*--')
        plt.xlabel('Number of Iterations [n]')
        plt.ylabel('Residuals [res]')
        plt.xlim([1,15])
        plt.legend(('Residuals per number of iterations'), loc='upper right')
        plt.show()
        return x
    print('No convergence after %d iterations!' % (N))
