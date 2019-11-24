import sys
import numpy as np
from Newton_Hook import Newton_Hook

n_iteration_max = 1000
trust_region = 0.5
trust_region_min = 1e-15
Lambda = 1.0
N_Function = 200
# x_0 = np.random.uniform(1,1.5,(N_Function,1))
x_0 = 1.25 * np.ones((N_Function,1))
alpha = 0.5                 # Reduction factor for trust region
beta = 2.0                 # Increment factor for trust region
tolerance_function = 1e-6
tolerance_variable = 1e-6

Newton_Hook(trust_region,trust_region_min,n_iteration_max,x_0,Lambda,N_Function,alpha,beta,tolerance_function,tolerance_variable)
