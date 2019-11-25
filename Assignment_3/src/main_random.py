## Numerical Analysis Assignment 3
## Date: 24 November 2019
## Main file to specify parameters and execute Newton-Hook method using intial estimate from uniform random sampling.
## Authors: Parikshit Bajpai, Marcos Machado

import numpy as np
from Newton_Hook import Newton_Hook

Lambda = 1.0                    # Parameter $\lambda$ used in function
N_Function = 25                 # Number of equations in the system

x_0 = np.random.uniform(1,1.5,(N_Function,1))   # Initial estimate

n_iteration_max = 1000          # Maximum number of Newton-Hook iterations

trust_region = 1.0              # Initial trust region
trust_region_min = 1e-12        # Minimum trust region

alpha = 0.5                     # Reduction factor for trust region
beta = 2.0                      # Increment factor for trust region

tolerance_function = 1e-6       # Tolerance for Newton residual
tolerance_variable = 1e-6       # Tolerance for Newton-Hook error

# Call Newton-Hook to find the roots.
x_n = Newton_Hook(trust_region,trust_region_min,n_iteration_max,x_0,Lambda,N_Function,alpha,beta,tolerance_function,tolerance_variable)
