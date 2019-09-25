# LUb LU decomposition without pivoting for matrix with zeros below bth sub
import scipy
import math
import copy

def LU(A):
    ok = 1                                              # set to 0 only if there is a zero pivot
    small = 1E-12                                       # numbers smaller than this are considered zero
    n = scipy.shape(A)[0]                               # extract number of rows
    U = copy.copy(A)                                    # initialize U and L
    L = scipy.identity(n)
    for j in range(1,n):                                # loop over columns
        for i in range(j+1,n+1):                        # loop over rows below diagonal
            if abs(U[j-1,j-1]) < small:                 # check for zero pivot
                print("Near-zero pivot element!")
                ok = 0
                break
            L[i-1,j-1]=U[i-1,j-1]/U[j-1,j-1];           # Gauss elimination
            for k in range(j,n+1):
                U[i-1,k-1] = U[i-1,k-1] - L[i-1,j-1] * U[j-1,k-1]
    return L,U,ok

