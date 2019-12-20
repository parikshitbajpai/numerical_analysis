# Compute the residual vector for the BVP u u' - nu u'' = 0, u(0)=L, u(1)=R. Discretized using finite differencing.
# By L van Veen, OnTechU, 2019.
import numpy as np
from make_diff_mat import D1, D2

def compute_F(u,x0,x1,L,R,N,nu):
    h = (x1 - x0) / float(N + 1)
    D = D1(x0,x1,N)
    DD = D2(x0,x1,N)
    v = D @ u
    F = u * v - nu * DD @ u
    F[0] -= L*u[0] / (2.0*h) + nu * L/(h**2)
    F[N-1] -= -u[N-1]*R / (2.0*h) + nu * R/(h**2)
    return F
