import numpy as np
import scipy as scipy
from copy import copy
from Functions import Function
from Functions import Jacobian
from Optimise import Optimise_direction_vector
from Test_Step import Test_Step

def Newton_Hook(trust_region,trust_region_min,n_iteration_max,x_0,Lambda,N_Function,alpha,beta,tolerance_function,tolerance_variable):
    n_iteration = 0
    x_n = copy(x_0)
    function = np.zeros((N_Function,1))
    jacobian = np.zeros((N_Function,N_Function))
    direction_vector = np.zeros((N_Function,1))
    converged = 0
    while not(converged):
        if n_iteration > n_iteration_max or trust_region < trust_region_min:
            print('Newton Hook failed to converge. Solution not found.')
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

        if residual < tolerance_function and error < tolerance_variable:
            converged = 1

        return x_n
