## Numerical Analysis Assignment 1
## Date: 28 September 2019
## This file computes the determinant of a matrix using LU decomposition
## Authors: Parikshit Bajpai, Marcos Machado

import scipy

## The following function computes the determinant of a triangular matrix
## as the product of diagonal elements.
## Function name: determinant_LUP
## Input: Matrix (A)
## Output: Determinant(A)
def determinant_LUP(A):
    n = scipy.shape(A)[0]
    determinant = 1.0
    for k in range(0,n):
        determinant*=A[k,k]
    return determinant
