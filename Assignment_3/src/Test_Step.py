## Numerical Analysis Assignment 3
## Date: 24 November 2019
## This file checks whether a selected step is acceptable or not.
## Authors: Parikshit Bajpai, Marcos Machado

import numpy as np
from copy import copy
from Functions import Function

def Test_Step(x_n,direction_vector,residual,Lambda,N_Function):
    x_test = copy(x_n)
    x_test = x_test + direction_vector                      # New approximation

    function_test = Function(x_test,Lambda,N_Function)

    residual_test = np.linalg.norm(function_test,2)         # Residual at new approximation.

    # If the residual is less than at previous iteration accept the new step else reject.
    if residual_test <= residual:
        accept = 1
    else:
        accept = 0

    return accept
