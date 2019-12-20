# Compute the Newton-Raphson update step using GMRES. By L. van Veen, 2019, OnTechU.
# The equation is P^(-1) J P^(-t) P^t du = - P^(-1) F.
import numpy as np
from copy import copy
from compute_F import compute_F
from mult_by_A import mult_by_A
from scipy.sparse.linalg import LinearOperator
from scipy.sparse.linalg import gmres
from mult_by_Pinv import mult_by_Pinv
from mult_by_PTinv import mult_by_PTinv
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
import scipy.sparse as sparse

# This class helps us gather diagnostics from GMRES.
class gmres_counter(object):
    def __init__(self, disp=True):
        self._disp = disp
        self.niter = 0
    def __call__(self, rk=None):
        self.niter += 1
# Enable these lines to have the GMRES residual printed after every iteration.
#        if self._disp:
#            print('iter %3i\trk = %s' % (self.niter, str(rk)))

def solve_for_NR_step(RHS,u,x0,x1,L,R,N,nu,tol_gmres_x,atol_gmres_y):
    # Compute the RHS for the pre-conditioned system.
    b = copy(RHS)
    b = mult_by_Pinv(b,x0,x1,N,nu)
    # Set up the linear operator.
    def mulA(v):
        return mult_by_A(v,u,x0,x1,L,R,N,nu)

    A = LinearOperator((N,N), matvec=mulA)
    # Initialize iteration counter to 0 and call GMRES.
    counter = gmres_counter()
    counter.__init__()
    # NOTE: GMRES tolerances are now hard-coded!

    print(tol_gmres_x * np.linalg.norm(b))
    print(atol_gmres_y)
    w, gmres_conv = gmres(A,b,maxiter=N,callback=counter,tol=tol_gmres_x,atol=atol_gmres_y)

    if gmres_conv > 0:
        print('No convergence in GMRES after %d iterations' % (gmres_conv))
    elif gmres_conv < 0:
        print('Illegal input or breakdown in GMRES')
    # We still have to solve P^t du = w...
    du = mult_by_PTinv(w,x0,x1,N,nu)
    return du, counter.niter
