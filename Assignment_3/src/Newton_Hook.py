## Numerical Analysis Assignment 3
## Date: 24 November 2019
## This file implements the Newton-Hook Algorithm for finding root of the function.
## Authors: Parikshit Bajpai, Marcos Machado

import numpy as np
import sys
from copy import copy
from Functions import Function
from Functions import Jacobian
from Optimise import Optimise_direction_vector
from Test_Step import Test_Step
import matplotlib.pyplot as plt

def Newton_Hook(trust_region,trust_region_min,n_iteration_max,x_0,Lambda,N_Function,alpha,beta,tolerance_function,tolerance_variable):
    n_iteration = 0
    x_n = copy(x_0)
    function = np.zeros((N_Function,1))
    jacobian = np.zeros((N_Function,N_Function))
    direction_vector = np.zeros((N_Function,1))
    converged = 0
    iteration_history = []                              # Stores residual and error at each iteration.

    while not(converged):
        if n_iteration > n_iteration_max:
            print('Maximum number of Newton-Hook iterations reached.')
            break
        if trust_region < trust_region_min:
            print('Size of trust region (%e) is smaller than minimum allowed (%e).' % (trust_region,trust_region_min))
            break

        # Find Newton Step
        function = Function(x_n,Lambda,N_Function)
        jacobian = Jacobian(x_n,Lambda,N_Function)
        direction_vector = - np.linalg.solve(jacobian,function)
        Newton_step = np.linalg.norm(direction_vector,2)
        residual = np.linalg.norm(function,2)

        # Test Newton-step if within trust region
        if Newton_step < trust_region:
            if Test_Step(x_n,direction_vector,residual,Lambda,N_Function):
                x_n += direction_vector     # Update approximation if step accepted
                n_iteration += 1
            else:
                trust_region *= alpha       # Reduce trust region by factor $\alpha$ if step not accepted

        # Find optimum direction vector and step if Newton-step is outside trust region.
        else:
            direction_vector = Optimise_direction_vector(x_n,Lambda,N_Function,trust_region)        # Compute new direction vector
            if Test_Step(x_n,direction_vector,residual,Lambda,N_Function):                          # Test new direction vector
                x_n += direction_vector     # Update approximation if step accepted
                trust_region *= beta        # Increase trust region by factor $\beta$ if the optimised direction vector is accepted
                n_iteration += 1
            else:
                trust_region *= alpha       # Reduce trust region by factor $\alpha$ if step not accepted

        function = Function(x_n,Lambda,N_Function)      # Evaaluate f(x_n)
        residual = np.linalg.norm(function,2)           # Residual = ||f(x_n)||_2
        error = np.linalg.norm(direction_vector,2)      # Error = ||dx||_2

        iteration_history.append([n_iteration,Newton_step,residual,error,trust_region])

        # Check for convergence
        if residual < tolerance_function and error < tolerance_variable:
            converged = 1
            break

    # If converged, plot and return x_n
    if converged:
        iteration_history = np.asarray(iteration_history)
        fig, ax=plt.subplots()
        ax.loglog(iteration_history[:,0],iteration_history[:,1],color='red',linestyle='dashed',marker='o',markersize=5.0,linewidth=1.5,label='Newton step size')
        ax.loglog(iteration_history[:,0],iteration_history[:,2],color='green',linestyle='dashed',marker='D',markersize=5.0,linewidth=1.5,label='Residual')
        ax.loglog(iteration_history[:,0],iteration_history[:,3],color='blue',linestyle='dashed',marker='v',markersize=5.0,linewidth=1.5,label='Error')
        ax.loglog(iteration_history[:,0],iteration_history[:,4],color='black',linestyle='dashed',marker='s',markersize=5.0,linewidth=1.5,label='Trust region')
        plt.legend()
        plt.tight_layout()
        plt.show()
        return x_n
    # If not converged, ensure graceful exit. 
    else:
        sys.exit('Newton-Hook failed to converge after %d iteration.' % (n_iteration))
