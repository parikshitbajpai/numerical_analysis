## Numerical Analysis Assignment 3
## Date: 24 November 2019
## This file computes parameters A and B used in the rational Newton method
## Authors: Parikshit Bajpai, Marcos Machado

import numpy as np

def Compute_A(Lagrange_multiplier_n,N_Function,a,b):
    A = 0.0
    numerator = 0.0
    denominator = 0.0
    for i in range(N_Function):
        numerator += a[i] / (b[i]+Lagrange_multiplier_n)**2.0
        denominator += a[i] / (b[i]+Lagrange_multiplier_n)**3.0
    A = numerator**2.0 / (2.0*denominator)
    return A

def Compute_B(Lagrange_multiplier_n,N_Function,a,b):
    B = 0.0
    numerator = 0.0
    denominator = 0.0
    for i in range(N_Function):
        numerator += a[i] / (b[i] + Lagrange_multiplier_n)**2.0
        denominator += a[i] / (b[i] + Lagrange_multiplier_n)**3.0
    B = (numerator / (2.0*denominator)) - Lagrange_multiplier_n
    return B
