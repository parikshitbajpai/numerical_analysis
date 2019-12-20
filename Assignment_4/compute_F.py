# Compute the residual vector for the BVP u u' - nu u'' = 0, u(0)=L, u(1)=R. Discretized using finite differencing.
# By L van Veen, OnTechU, 2019.
import numpy as np
#from make_diff_mat import D1, D2

def compute_F(u,x0,x1,L,R,N,nu):
    h = (x1 - x0) / float(N + 1)
    #D = D1(x0,x1,N)
    #DD = D2(x0,x1,N)
    v = np.zeros((N,1))
    gamma = np.zeros((N,1))

    v[0] = u[1]
    for i in range(1,N-1):
        v[i]=u[i+1]-u[i-1]
    v[N-1] = -u[N-1]
    v = v/(2*h)

    gamma[0] = -2*u[0] + u[1]
    for i in range(1,N-1):
        gamma[i] = -2*u[i] + u[i+1] + u[i-1]
    gamma[N-1] = u[N-2]-2*u[N-1]
    gamma = gamma / (h**2)

    F = u * v - nu * gamma
    F[0] -= L*u[0] / (2.0*h) + nu * L/(h**2)
    F[N-1] -= -u[N-1]*R / (2.0*h) + nu * R/(h**2)
    return F
