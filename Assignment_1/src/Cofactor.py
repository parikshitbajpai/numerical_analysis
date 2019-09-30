## Numerical Analysis Assignment 1
## Date: 28 September 2019
## This file computes the determinant of a matrix using cofactors
## Authors: Parikshit Bajpai, Marcos Machado

import numpy as np
import scipy
import scipy.linalg
import math

## The following function recursively computes the determinant of a matrix
## using cofactors.
## Function name: determinant_cofactor
## Input: Matrix (A)
## Output: Determinant(A)
def determinant_cofactor(A):
    n = scipy.shape(A)[0]
    det_n=0
    if n==2:
        det_2=A[0,0]*A[1,1]-(A[1,0]*A[0,1])
        return det_2
    else:
        for i in range (0,n):
            det_n+=((-1)**(i))*A[0,i]*determinant_cofactor(comp_minor(A,n,0,i))
    return det_n

## The following function computes the minor matrix ((n-1)*(n-1))
## of matrix A(n*n) corresponding to row r and column c.
## Function name: comp_minor
## Input: Matrix (A), Dimension of A (n), Row (r), Column (c)
## Output: Minor matrix
def comp_minor(A,n,r,c):
    minor=np.zeros((n-1,n-1))           # Initialize minor matrix
    ri = 0                              # Row index for the minor matrix
    rj = 0                              # Column index for the minor matrix

    for i in range (0,n):
        rj=0
        if (i==r):
            continue
        for j in range (0,n):
            if (j==c):
                continue
            minor[ri,rj]=A[i,j]
            rj +=1
        ri +=1
    return minor
