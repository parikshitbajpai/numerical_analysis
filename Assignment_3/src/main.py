import numpy as np
from Newton_Hook import Newton_Hook

n_iteration_max = 1000
trust_region = 0.1
trust_region_min = 1e-10
Lambda = 1.05
N_Function = 10
x_0 = np.zeros(N_Function)
alpha = 0.5                 # Reduction factor for trust region

Newton_Hook(trust_region_min,n_iteration_max,x_0,Lambda,N_Function,alpha)
