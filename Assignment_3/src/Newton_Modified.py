## Numerical Analysis Assignment 3
## Date: 24 November 2019
## This file implements the Newton algorithm with rational approximation for finding the Lagrange multiplier of optimisation problem.
## Authors: Parikshit Bajpai, Marcos Machado

import numpy as np
import sys
from copy import copy
from Compute import Compute_A
from Compute import Compute_B
from Functions import Lagrangian

def Newton_Modified(Lagrange_multiplier_0,delta,a,b,N_Function):
    converged = 0
    eps_f = 1e-3                # Tolerance for rational Newton method is relatively large as discussed in class.
    eps_x = 1e-3                # Tolerance for rational Newton method is relatively large as discussed in class.
    n_iterations_Newton = 1000
    residual = 0.0
    Lagrange_multiplier_n = copy(Lagrange_multiplier_0)

    for i in range(n_iterations_Newton):
        r = Lagrangian(Lagrange_multiplier_n,a,b,delta,N_Function)
        residual = Compute_A(Lagrange_multiplier_n,N_Function,a,b)/delta - Compute_B(Lagrange_multiplier_n,N_Function,a,b) - Lagrange_multiplier_n
        Lagrange_multiplier_n += residual

        # Check convergence
        if abs(r) < eps_f and abs(residual) < eps_x:
            converged = 1
            break

    # Return Lagrange multiplier if converged.
    if converged:
        return Lagrange_multiplier_n
    # Ensure graceful exit if Lagrange multiplier not found.
    else:
        print('=============== Rational Newton ===============')
        print('Error = %e' % (abs(residual)))
        print('Residual = %e' % (abs(r)))
        sys.exit('No convergence after %d Newton iterations. Lagrange Multiplier could not be found.' % (n_iterations_Newton))
