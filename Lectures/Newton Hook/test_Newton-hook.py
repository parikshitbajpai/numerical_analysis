# Test script for Newton-hook iteration. Programmed in lecture 12.
import numpy as np
from Newton_hook import Newton_hook
from functions import fN, DfN
# For comparison:
from Newton_Raphson import Newton_Raphson
# For plotting:
import matplotlib.pyplot as plt

# Convergece criteria:
tol_f = 1e-12
tol_x = 1e-12

# Initial and minimal size of trust region:
delta = 0.001
delta_min = 1e-10

# Factors to decrease/increase the trust region:
alpha = 0.8
beta = 1.2

# Number of equations to consider and system parameter:
N = 1500
lam = 5e-1

# Initial guess (exact solution for lam = 0)
x0 = np.ones((N,1))

# Maximal number of iterations:
N_max = 1000

# Auxiliary definition of the test problem with only one argument:
def G(x):
    return fN(x,N,lam)
def DG(x):
    return DfN(x,N,lam)

x,diag1 = Newton_hook(x0,G,DG,delta,N_max,tol_f,tol_x,alpha,beta,delta_min)
print(x)

x,diag2 = Newton_Raphson(G,DG,x0,tol_f,tol_x,N)
print(x)

plt.loglog(diag1[:,0],diag1[:,1],'-k')
plt.loglog(diag1[:,0],diag1[:,2],'-b')
plt.loglog(diag1[:,0],diag1[:,3],'-r')
plt.show()
plt.loglog(diag2[:,0],diag2[:,1],'-k')
plt.loglog(diag2[:,0],diag2[:,2],'-b')
plt.show()
