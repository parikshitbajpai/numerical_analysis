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
from Determinant_LUP import determinant_LUP

ntrials = 8                                         # Number of trials
wtime = np.zeros((ntrials,2))                       # Array to store wall time
error_rel = np.zeros((ntrials,2))                   # Array to store relative error
error_absolute = np.zeros((ntrials,2))              # Array to store absolute error
condition_number = np.zeros((ntrials,2))            # Array to store condition number
n=2                                                 # Initial matrix size

for k in range(0,ntrials):
    A = np.random.rand(n,n)                         # Generate random matrix

    ## The following commands use the LUP decomposition to compute determinant of A.
    start_lu = time.time()                          # Get start time for LUP
    det_lu = determinant_LUP(A)
    elapsed_lu = time.time()-start_lu               # Elapsed time using LUP

    # Print wall time to screen
    print('Size = %d, Time_LU = %e' % (n,elapsed_lu))

    ## The following commands use numpy to compute determinant of A and is assumed to be the "correct" value of determinant.
    det_np = np.linalg.det(A)

    ## The absolute errors are computed with respect to determinant using numpy which is assumed to be the 'true' value.
    error_absolute[k,0] = n
    error_absolute[k,1] = abs(det_lu-det_np)

    ## The relative errors are computed with respect to determinant using numpy which is assumed to be the 'true' value.
    error_rel[k,0] = n
    error_rel[k,1] = abs(det_lu-det_np)/abs(det_np)

    ## The following array are used to save the results for time.
    wtime[k,0] = n
    wtime[k,1] = elapsed_lu

    ## Increase matrix size for subsequent trial.
    n *= 2

## Arrays to plot the orders of complexity
x = np.arange(256)                                          # Array of natural numbers to plot complexity
y_LU = [math.pow(i,3) for i in x]                           # Complexity of LU decomposition

## The following commands plot the relevant graphs
## This plot shows the computation time versus the matrix size. Also shows the order of complexity for comparison.
plt.loglog(wtime[:,0],wtime[:,1],'-o',y_LU,'--')
plt.title('Computation time vs. matrix size')
plt.xlabel('Matrix size [n]')
plt.ylabel('Time [s]')
plt.xlim([2,256])
plt.ylim(bottom=0.1/10000000,top=100000000)
plt.legend(('Wall Time: LUP','Order of Complexity: n^3'), loc='upper left')
plt.show()

# This plot shows the absolute error with respect to 'true' determinant computed using numpy.
plt.loglog(error_absolute[:,0],error_absolute[:,1],'-o')
plt.title('Absolute errors vs. matrix size')
plt.xlabel('Matrix size [n]')
plt.ylabel('Absolute error [unitless]')
plt.xlim([2,256])
plt.show()

## This plot shows the relative errors with respect to 'true' determinant computed using numpy.
plt.loglog(error_rel[:,0],error_rel[:,1],'-o')
plt.title('Relative errors vs. matrix size')
plt.xlabel('Matrix size [n]')
plt.ylabel('Relative error [unitless]')
plt.show()
