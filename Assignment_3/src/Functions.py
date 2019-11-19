import numpy as np
import math

def Function(x_n,Lambda,N_Function):
    function = np.zeros((N_Function,1))
    for i in range(N_Function):
        function[i] = x_n[i] - math.exp(Lambda * math.cos(i * np.sum(x_n)))
    return function

def Jacobian(x_n,Lambda,N_Function):
    jacobian = np.identity(N_Function)
    sum_function_terms = np.sum(x_n)
    for i in range(N_Function):
        jacobian[i,:] = jacobian[i,:] + (i + 1.0) * Lambda * math.sin(i * sum_function_terms) * math.exp(Lambda * math.cos(i * sum_function_terms))
    return jacobian

def Lagrangian(Lagrange_multiplier,a,b,Delta,N_Function):
    f = -Delta
    for i in range(N_Function):
        f += a[i] / (b[i] + Lagrange_multiplier)**2.0
    return f

def Derivative_Lagrangian(Lagrange_multiplier,a,b,Delta,N_Function):
    fp = 0.0
    for i in range(N_Function):
        fp += (-2.0 * a[i]) / (b[i] + Lagrange_multiplier)**3.0
    return fp
