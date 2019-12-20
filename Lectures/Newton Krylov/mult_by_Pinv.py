# Compute the product of a given vector with P^(-1) where P = sqrt(nu) L
# so that P P^t = nu L L^t = - nu D^(2). 
# By L. van Veen, 2019 OnTechU. 
import numpy as np

# Note: elements of the Cholesky decomposition of D^(2) are re-computed every time this function is called.
# They can be pre-computed and stored for a slight speed-up.
def d(i,h,nu):
    # Diagonal element of P on i-th row. NOTE: i is the row index, not the Python array index!
    return np.sqrt(nu*float(i+1)/float(i)) / h
def s(i,h,nu):
    # Sub-diagonal element of P on i-th row. NOTE: i is the row index, not the Python array index!
    return -np.sqrt(nu*float(i-1)/float(i)) / h

def mult_by_Pinv(v,x0,x1,N,nu):
    h = (x1 - x0) / float(N + 1)
    w = np.zeros((N,1))
    w[0] = v[0] / d(1,h,nu)
    for i in range(1,N):
        w[i] = (v[i] - s(i+1,h,nu) * w[i-1]) / d(i+1,h,nu)
    return w
