## Numerical Analysis Assignment 1
## Date: 02 October 2019
## Main script for running the LUP decomposition method for finding the determinant of a n*n matrix
## Authors: Parikshit Bajpai

import numpy as np
import time                                         # For timing
import scipy
import math
import matplotlib.pyplot as plt                     # For plotting
import matplotlib.pylab as plt
from LUP import LUP
from Determinant_LUP import determinant_LUP

ntrials = 10                                         # Number of trials
wtime = np.zeros((ntrials,2))                       # Array to store wall time
error_rel = np.zeros((ntrials,2))                   # Array to store relative error
n=2                                                 # Initial matrix size

for k in range(0,ntrials):
    A = np.random.rand(n,n)

    ## The following commands use the LUP decomposition to compute determinant of A.
    start_lu = time.time()                          # Get start time for LUP
    L,U,P,par = LUP(A)
    det_lu = determinant_LUP(L)*determinant_LUP(U)*par
    elapsed_lu = time.time()-start_lu               # Elapsed time using LUP

    ## The following commands use numpy to compute determinant of A and is assumed to be the "correct" value of determinant.
    det_np = np.linalg.det(A)

    ## The relative errors are computed with respect to determinant using numpy which is assumed to be the 'true' value.
    error_rel_lu = abs(det_lu-det_np)/abs(det_np)           # Rel Error using LUP

    print('Size = %d, Time_LU = %e' % (n,elapsed_lu))

    ## The following parts are used to save the results for time and error.
    wtime[k,0] = n                                          # Wall times
    wtime[k,1] = elapsed_lu

    ## The relative errors are computed with respect to determinant using numpy which is assumed to be the 'true' value.
    error_rel[k,0] = n                                      # Relative errors
    error_rel[k,1] = error_rel_lu

    ## Increase matrix size for subsequent trial.
    n *= 2

## Arrays to plot the orders of complexity
x = np.arange(1024)                                          # Array of natural numbers to plot complexity
y_LU = [math.pow(i,3) for i in x]                           # Complexity of LU decomposition

## The following commands plot the relevant graphs
## This plot shows the computation time versus the matrix size. Also shows the order of complexity for comparison.
plt.loglog(wtime[:,0],wtime[:,1],'-o',y_LU,'--')
plt.title('Computation time vs. matrix size')
plt.xlabel('Matrix size [n]')
plt.ylabel('Time [s]')
plt.xlim([2,1024])
plt.ylim(bottom=0.1/10000000,top=100000000)
plt.legend(('Wall Time: LUP','Order of Complexity: n^3'), loc='upper left')
plt.show()

## This plot shows the relative errors with respect to 'true' determinant computed using numpy.
plt.loglog(error_rel[:,0],error_rel[:,1],'-o')
plt.title('Relative errors vs. matrix size')
plt.xlabel('Matrix size [n]')
plt.ylabel('Relative error [unitless]')
plt.legend(('Relative error: LUP'))
plt.show()
