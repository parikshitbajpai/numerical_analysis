## Numerical Analysis Assignment 1
## Date: 28 September 2019
## This file computes the determinant of a matrix using LU decomposition
## Authors: Parikshit Bajpai, Marcos Machado

import scipy
from LUP import LUP

## The following function computes the determinant of a square matrix using LUP factorisation
## Function name: determinant_LUP
## Input: Matrix (A)
## Output: Determinant(A)
def determinant_LUP(A):
    L,U,P,par = LUP(A)
    determinant = determinant_triangular(L)*determinant_triangular(U)*par
    return determinant

## The following function computes the determinant of a triangular matrix
## as the product of diagonal elements.
## Function name: determinant_triangular
## Input: Triangular matrix (A)
## Output: Determinant(A)
def determinant_triangular(A):
    n = scipy.shape(A)[0]
    determinant = 1.0
    for k in range(0,n):
        determinant*=A[k,k]
    return determinant
