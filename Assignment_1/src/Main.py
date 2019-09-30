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

ntrials = 7                                         # nr. of trials
wtime_lu=np.zeros((ntrials,2))                      # array to store wall times
wtime_cofactor=np.zeros((ntrials,2))
accuracy = np.zeros((ntrials,3))                    # array to store accuracy measures
error_rel = np.zeros((ntrials,3))                   # array to store error measures
n=2
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

    ## The following parts are used for analysis of results.
    check = np.linalg.norm(np.matmul(L,U)-np.matmul(P,A))
    condition = np.linalg.cond(A,2)                         # Condition number of matrix A
    error_rel_lu = abs(det_lu-det_np)/abs(det_np)           # Rel Error using LUP
    error_rel_cof = abs(det_cofactor-det_np)/abs(det_np)    # Rel Error using cofactor

    print('n = %d, error = %e, K(A) = %e, t_lu = %e , t_cofactor = %e' % (n,check,condition,elapsed_lu,elapsed_cofactor))
    #print('n = %d, error = %e, K(A) = %e, t_lu = %e'  % (n,check,condition,elapsed_lu))
    #print('n = %d, K(A) = %e, t_cofactor = %e' % (n,condition,elapsed_cofactor))

    ## Increase matrix size for subsequent trial.
    n += 2

    ## The following parts are used to save the results for time and error
    wtime_lu[k,0] = n                                       # Wall time for LUP
    wtime_lu[k,1] = elapsed_lu

    wtime_cofactor[k,0] = n                                 # Wall time for cofactor
    wtime_cofactor[k,1] = elapsed_cofactor

    error_rel[k,0] = n                                      # Relative errors
    error_rel[k,1] = error_rel_lu
    error_rel[k,1] = error_rel_cof

    accuracy[k,0] = n                                       # Accuracy
    accuracy[k,1] = check
    accuracy[k,2] = condition

## The following commands plot the relevant graphs
n = np.arange(100)                                          # Theoretical complexity of cofactor method
y_factorial = [math.factorial(nn) for nn in n]              

x_power3 = np.array(range(16))                              # Theoretical complexity of LU decomposition
y_power3 = x_power3**3 / 10000

plt.loglog(wtime_cofactor[:,0],wtime_cofactor[:,1],'-*',wtime_lu[:,0],wtime_lu[:,1],'-*',y_factorial,'--',y_power3,'--')
plt.title('Time as a function of size of the Matrix (n x n)')
plt.xlabel('Matrix size (n)')
plt.ylabel('Time in seconds (s)')
plt.xlim([0,16])
plt.ylim([0,1000000000000])
plt.legend(('Computation: Cofactor','Computation: LUP','Order of Complexity: n!','Order of Complexity: n^3'), loc='lower left')
plt.show()

plt.loglog(accuracy[:,0],accuracy[:,1],'-r')
plt.loglog(accuracy[:,0],accuracy[:,2],'-k')
