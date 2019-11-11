## Numerical Analysis Assignment 2
## Date: 8 November 2019
## This file computes the terms A and B of the rational function.
## Authors: Parikshit Bajpai, Marcos Machado

import numpy as np
from copy import copy

## A and B are computed as a solution of a linear system where the equations are:
## 1) functions f(x_n) and g(x_n) are equal, and,
## 2) the derivatives fp(x_n) and gp(x_n) are equal
def compute_A(x_n,M,a,b):
    A = 0.0
    numerator = 0.0
    denominator = 0.0
    for i in range(M):
        numerator += a[i] / (b[i]+x_n)**2.0
        denominator += a[i] / (b[i]+x_n)**3.0
    A = numerator**2.0 / (2.0*denominator)
    return A

def compute_B(x_n,M,a,b):
    B = 0.0
    numerator = 0.0
    denominator = 0.0
    for i in range(M):
        numerator += a[i] / (b[i]+x_n)**2.0
        denominator += a[i] / (b[i]+x_n)**3.0
    B = (numerator / (2.0*denominator)) - x_n
    return B
