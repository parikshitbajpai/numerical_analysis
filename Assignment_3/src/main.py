import numpy as np
from Newton_Hook import Newton_Hook

n_iteration_max = 1000
trust_region = 0.1
trust_region_min = 1e-10
Lambda = 1.05
N_Function = 10
x_0 = np.zeros((N_Function,1))
alpha = 0.5                 # Reduction factor for trust region
beta = 1.2                  # Increment factor for trust region
tolerance_function = 1e-5
tolerance_variable = 1e-5

print(Newton_Hook(trust_region,trust_region_min,n_iteration_max,x_0,Lambda,N_Function,alpha,beta,tolerance_function,tolerance_variable))
