# Author: L. van Veen, UOIT, 2018
# PA=LU decomposition that keeps track of the parity of the permutation (even=1, odd=-1)

import scipy
import scipy.linalg
from copy import copy

# note: indeces i,j and k are used as matrix indeces (starting from 1) while s is used as python array index (starting from 0)
def LUP(A):
    n = scipy.shape(A)[0]                         # extract matrix size
    U = copy(A)                                   # copy content of A (avoid linking U and A)
    L = scipy.identity(n)                         # initialize L and P
    P = scipy.identity(n)
    par = 1                                       # initial permutation (identity) is even

    for k in range(1,n):
        s = scipy.argmax(abs(U[k-1:n,k-1]))+k-1   # find pivot element
        if s != k-1:                              # if the pivot is not on the diagonal...
            par = -par                            # change parity
            U = swap(U,s,k-1,n)                   # swap rows of U
            if k>1:                               # swap rows of L left of diagonal element
                L = swap(L,s,k-1,k-1)
            P = swap(P,s,k-1,n)                   # swap rows of P
        for j in range(k+1,n+1):                  # Gauss elimination of rows below pivot
            L[j-1,k-1] = U[j-1,k-1]/U[k-1,k-1]
            for i in range(k,n+1):
                U[j-1,i-1]=U[j-1,i-1] - L[j-1,k-1]*U[k-1,i-1]
                U[j-1,i-1]=round(U[j-1,i-1],14)
    return L,U,P,par

def swap(M,i,j,k):
# swap rows i and j from column 0 up to (but not including) k
# indeces in this function are used as python array indeces (starting from 0)
    dum = copy(M[i,0:k])
    M[i,0:k] = copy(M[j,0:k])
    M[j,0:k] = copy(dum)
    return M
