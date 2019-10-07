import numpy as np
import scipy
import scipy.linalg
import math

def limit(x,tolerance):
    y_last = 1.0
    k = 1.0
    n_max = 100000
    err_rel = 1.0
    n = 0
    while (err_rel > tolerance):
        y = (1 + (x / k))**k
        err_rel = abs(y-y_last)/abs(y)
        y_last = y
        k += 1
        n += 1
        if (n > n_max):
            print("Limit: Maximum no. of iterations reached. Solution did not converge")
            break
    return y
