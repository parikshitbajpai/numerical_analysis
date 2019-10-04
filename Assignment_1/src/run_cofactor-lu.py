## Numerical Analysis Assignment 1
## Date: 28 September 2019
## Main script for comparing the cofactor and LUP decomposition methods for finding the determinant of a n*n matrix
## Authors: Parikshit Bajpai, Marcos Machado

import numpy as np
import time                                         # For timing
import scipy
import math
import matplotlib.pyplot as plt                     # For plotting
import matplotlib.pylab as plt
from LUP import LUP
from Determinant_LUP import determinant_LUP
from Cofactor import comp_minor
from Cofactor import determinant_cofactor

ntrials = 6                                         # Number of trials
wtime = np.zeros((ntrials,3))                       # Array to store wall times
error_rel = np.zeros((ntrials,3))                   # Array to store relative errors
error_absolute = np.zeros((ntrials,4))              # Array to store difference in errors
n=2                                                 # Initial matrix size

for k in range(0,ntrials):
    A = np.random.rand(n,n)

    ## The following commands use the LUP decomposition to compute determinant of A.
    start_lu = time.time()                          # Get start time for LUP
    L,U,P,par = LUP(A)
    det_lu = determinant_LUP(L)*determinant_LUP(U)*par
    elapsed_lu = time.time()-start_lu               # Elapsed time using LUP

    ## The following commands use the cofactor method to compute determinant of A.
    start_cofactor = time.time()                    # Get start time for cofactor
    det_cofactor = determinant_cofactor(A)
    elapsed_cofactor = time.time()-start_cofactor   # Elapsed time using LUP

    ## The following commands use numpy to compute determinant of A and is assumed to be the "correct" value of determinant.
    det_np = np.linalg.det(A)

    ## Difference between determinant computed from LU decomposition and Cofactor methods.
    error_absolute[k,0] = n
    error_absolute[k,1] = abs(det_lu - det_np)
    error_absolute[k,2] = abs(det_cofactor - det_np)
    error_absolute[k,3] = abs(det_lu - det_cofactor)

    ## The relative errors are computed with respect to determinant using numpy which is assumed to be the 'true' value.
    error_rel_lu = abs(det_lu-det_np)/abs(det_np)           # Rel Error using LUP
    error_rel_cof = abs(det_cofactor-det_np)/abs(det_np)    # Rel Error using cofactor

    print('Size = %d, Time_LU = %e , Time_Cofactor = %e' % (n,elapsed_lu,elapsed_cofactor))

    ## The following parts are used to save the results for time and error.
    wtime[k,0] = n                                          # Wall times
    wtime[k,1] = elapsed_lu
    wtime[k,2] = elapsed_cofactor

    ## The relative errors are computed with respect to determinant using numpy which is assumed to be the 'true' value.
    error_rel[k,0] = n                                      # Relative errors
    error_rel[k,1] = error_rel_lu                           # LU factorization
    error_rel[k,2] = error_rel_cof                          # Cofactor matrix

    ## Increase matrix size for subsequent trial.
    n += 2                                                  # Using n += 2 since cofactor method takes very long for n >= 14

## Arrays to plot the orders of complexity
x = np.arange(100)                                          # Array of natural numbers to plot complexity
y_cofactor = [math.factorial(i) for i in x]                 # Complexity of Cofactor method
y_LU = [math.pow(i,3) for i in x]                           # Complexity of LU decomposition

## The following commands plot the relevant graphs
## This plot shows the computation time versus the matrix size. Also shows the order of complexity for comparison.
plt.loglog(wtime[:,0],wtime[:,1],'-o',wtime[:,0],wtime[:,2],'-o',y_LU,'--',y_cofactor,'--')
plt.title('Computation time vs. matrix size')
plt.xlabel('Matrix size [n]')
plt.ylabel('Time [s]')
plt.xlim([2,12])
plt.ylim(bottom=0.1/10000000,top=100000000)
plt.legend(('Wall Time: LUP','Wall Time: Cofactor','Order of Complexity: n^3','Order of Complexity: n!'), loc='upper left')
plt.show()

# This plot shows the difference in the values of determinants computed using the two methods.
plt.loglog(error_absolute[:,0],error_absolute[:,1],'-o',error_absolute[:,0],error_absolute[:,2],'-o',error_absolute[:,0],error_absolute[:,3],'-*')
plt.title('Absolute errors vs. matrix size')
plt.xlabel('Matrix size [n]')
plt.ylabel('Absolute error [unitless]')
plt.legend(('Absolute error: LUP','Absolute error: Cofactor','Difference'))
plt.show()

## This plot shows the relative errors with respect to 'true' determinant computed using numpy.
plt.loglog(error_rel[:,0],error_rel[:,1],'-o',error_rel[:,0],error_rel[:,2],'-o')
plt.title('Relative errors vs. matrix size')
plt.xlabel('Matrix size [n]')
plt.ylabel('Relative error [unitless]')
plt.legend(('Relative error: LUP','Relative error: Cofactor'))
plt.show()
