# Main code for numerically solving the boundary value problem u u' - nu u'' = 0, u(0)=L, u(1)=R.
# Uses Newton-Raphson iteration with GMRES for the linear systems (also called Newton-Krylov).
# For MCSC6020G, by L. van Veen, 2019 OnTechU. 
import numpy as np
import matplotlib.pyplot as plt
from copy import copy
from exact_solution import exact
from NR_GMRES import NR

# Set domain and number of (interior) grid points.
x0 = 0.0
x1 = 1.0
N_grid = 1000

# Set constants of integration of exact solution.
A = 10.0
B = 0.1

# Set the viscosity.
nu = 0.01

# Find the left and right boundary values from the exact solution.
# NOTE: normally, one would set the boundary values and solve for A and B, this is just a short cut.
L = exact(x0,x0,x1,A,B,nu)
R = exact(x1,x0,x1,A,B,nu)

# Define the grid (u=L and u=R at leftmost and rightmost points).
grid = np.linspace(x0,x1,N_grid+2)
h = (x1 - x0) / float(N_grid + 1)

# Compute the exact solution for plotting. Solutions on the grid will be represented by column vectors of np.shape (N_grid,1) 
# on the interior points or (N_grid+2,1) for the full grid.
y_e = copy(grid)
for i in range(N_grid+2):
    y_e[i] = exact(grid[i],x0,x1,A,B,nu)
y_e = y_e.reshape((N_grid+2,1))

# Pick an initial guess. Now set to linear function.
def guess(x,x0,x1,L,R):
    return L + (R-L) * (x - x0) / (x1 - x0)

u0 = guess(grid[1:N_grid+1],x0,x1,L,R)
u0 = u0.reshape((N_grid,1))

# Set the tolerance for the residual and error of the Newton-Raphson iteration as well as the max nr of iterations.
tol_f = 1e-8
tol_x = 1e-8
Nmax = 15

# Call the Newton-Krylov routine.
u, res, err = NR(u0,tol_f,tol_x,Nmax,x0,x1,N_grid,L,R,nu)

# Plot the numerical and exact solution.
plt.plot(grid,y_e,'-k')
plt.plot(grid[1:N_grid+1],u,'-g')
plt.plot(grid[1:N_grid+1],u0,'-r')
plt.show()

# Plot the difference.
plt.plot(grid[1:N_grid+1],y_e[1:N_grid+1]-u,'-r')
plt.show()

print('Error in inf norm = %e' % (np.linalg.norm(y_e[1:N_grid+1]-u,np.inf)))

