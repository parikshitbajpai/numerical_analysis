import numpy as np
from copy import copy
import matplotlib.pylab as plt
from Compute import Compute_A
from Compute import Compute_B
from Functions import Lagrangian
from Functions import Derivative_Lagrangian

def Newton_Modified(Lagrange_multiplier_0,delta,a,b,N_Function):
    flag = 0
    eps_f = 1e-10
    eps_x = 1e-10
    n_iterations_Newton = 1000
    residual = 0.0
    Lagrange_multiplier_n = copy(Lagrange_multiplier_0)
    for i in range(n_iterations_Newton):
        r = Lagrangian(Lagrange_multiplier_n,a,b,delta,N_Function)
        residual = Compute_A(Lagrange_multiplier_n,N_Function,a,b)/delta - Compute_B(Lagrange_multiplier_n,N_Function,a,b) - Lagrange_multiplier_n
        Lagrange_multiplier_n += residual
        if abs(r) < eps_f and abs(residual) < eps_x:
            flag = 1
            break
    if flag==1:
        return Lagrange_multiplier_n
    print('No convergence after %d Newton iterations!' % (n_iterations_Newton))
