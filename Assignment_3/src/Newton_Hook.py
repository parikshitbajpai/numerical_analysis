import numpy as np
import scipy as scipy
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
    iteration_history = []

    while not(converged):
        if n_iteration > n_iteration_max or trust_region < trust_region_min:
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
                x_n += direction_vector
                n_iteration += 1
            else:
                trust_region *= alpha

        else:
            direction_vector = Optimise_direction_vector(x_n,Lambda,N_Function,trust_region)
            if Test_Step(x_n,direction_vector,residual,Lambda,N_Function):
                x_n += direction_vector
                trust_region *= beta
                n_iteration += 1
            else:
                trust_region *= alpha

        function = Function(x_n,Lambda,N_Function)
        residual = np.linalg.norm(function,2)
        error = np.linalg.norm(direction_vector,2)

        iteration_history.append([n_iteration,Newton_step,residual,error,trust_region])

        if residual < tolerance_function and error < tolerance_variable:
            converged = 1
            break

    if converged:
        iteration_history = np.asarray(iteration_history)
        fig, ax=plt.subplots()
        ax.loglog(iteration_history[:,0],iteration_history[:,1],'-r',label='Newton step size')
        ax.loglog(iteration_history[:,0],iteration_history[:,2],'-g',label='Residual')
        ax.loglog(iteration_history[:,0],iteration_history[:,3],'-b',label='Error')
        ax.loglog(iteration_history[:,0],iteration_history[:,4],'-k',label='Trust region')
        plt.legend()
        plt.tight_layout()
        plt.show()
        return x_n
    else:
        sys.exit('Newton-Hook failed to converge after %d iteration.' % (n_iteration))
