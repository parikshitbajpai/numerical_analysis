# Newton-Krylov iteration for the BVP u u' - nu u'' = 0, u(0)=L, u(1)=R discretized by finite differences.
# By L. van Veen, 2019 OnTechU. 

import numpy as np
from copy import copy
from compute_F import compute_F
from solve_for_NR_step import solve_for_NR_step

def NR(u0,tol_f,tol_x,Nmax,x0,x1,N,L,R,nu):
    conv = 0
    u = copy(u0)
    for i in range(Nmax):
        # Compute the residual vector.
        RHS = - compute_F(u,x0,x1,L,R,N,nu)
        # Solve linear system by GMRES.
        du, numits = solve_for_NR_step(RHS,u,x0,x1,L,R,N,nu)
        print('Nr. of GMRES iteration = %d' %(numits))
        # Apply the Newton-Raphson update step.
        u += du
        # Test for convergence.
        res = np.linalg.norm(RHS,2)
        err = np.linalg.norm(du,2)
        print('It %d res = %e err = %e' % (i,res,err))
        if res < tol_f and err < tol_x:
            conv = 1
            break
    if conv == 0:
        print('No convergence after %d iterations...' % (Nmax))
        

    return u,res,err
