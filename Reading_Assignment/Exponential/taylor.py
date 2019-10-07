# For Reading assignment.

import scipy
import scipy.linalg
from copy import copy
import numpy as np
import scipy
import math

def taylor(x,tolerance):
    y = 1.0
    k = 1.0
    n_max = 100000
    err_rel = 1.0
    n = 0
    while (err_rel > tolerance):
        term = (1.0 / math.factorial(k)) * (x**k)
        err_rel = abs(term)/abs(y)
        y += term
        k += 1
        n += 1
        if (n > n_max):
            print("Taylor: Maximum no. of iterations reached. Solution did not converge")
            break
    return y
