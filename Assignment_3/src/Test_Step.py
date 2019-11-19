import numpy as np
from copy import copy

def Test_Step(x_n,direction_vector,residual,Lambda,N_Function):
    x_test = copy(x_n)
    x_test = x_test + direction_vector
    function_test = Function(x_test,Lambda,N_Function)
    residual_test = np.linalg.norm(function_test,2)
    if residual_test <= residual:
        accept = 1
    else:
        accept = 0
    return accept
