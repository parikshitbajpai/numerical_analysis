## Numerical Analysis Assignment 3
## Date: 24 November 2019
## This file implements direction vector optimisation for Newton-Hook algorithm.
## Authors: Parikshit Bajpai, Marcos Machado

import numpy as np
from copy import copy
from Functions import Function
from Functions import Jacobian
from Newton_Modified import Newton_Modified

def Optimise_direction_vector(x_n,Lambda,N_Function,trust_region):
    a = np.zeros((N_Function,1))
    b = np.zeros((N_Function,1))
    U = np.zeros((N_Function,N_Function))
    S = np.zeros((N_Function,1))
    V_T = np.zeros((N_Function,N_Function))
    jacobian = Jacobian(x_n,Lambda,N_Function)

    U,S,V_T = np.linalg.svd(jacobian)               # Singular Value Decomposition

    function = Function(x_n,Lambda,N_Function)
    g = U.T @ function
    S = S.reshape(N_Function,1)

    for i in range(N_Function):
        b[i] = (S[i]**4)
        a[i] = b[i] * (g[i]**2)

    Lagrange_multiplier_0 = abs((np.amin(a))**2 / (2 * (np.amin(b))**2) * (1 / trust_region**2 - 1))        # Initial estimate of Lagrange multiplier based on a_min and b_min

    Lagrange_multiplier = Newton_Modified(Lagrange_multiplier_0,(trust_region**2),a,b,N_Function)           # Use rational Newton to find Lagrange Multiplier

    w = np.zeros((N_Function,1))
    for i in range(N_Function):
        w[i] = -S[i]**2 * g[i] / (S[i]**4 + Lagrange_multiplier)

    direction_vector = V_T.T @ w

    return direction_vector
