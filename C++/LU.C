//* This file is part of the LU decomposition program
//* Written for MCSC 6020G - Numerical Analysis (Fall 2019)
//*
//* Author - Parikshit Bajpai

#include <iostream>
#include <math.h>
#include <stdio.h>
#include "LU.h"

LU::tolerance = 1e-12; // Tolerance
void LU::LU(float &matrix[][]) {
  int n; // Size of matrix
  n = sizeof(matrix)/sizeof(matrix[0]);
  float U[n][n] = matrix;
  float L[n][n] = 0;
  for (size_t i = 0; i < n; i++) {
    L[i][i] = 1;
  }
  for (size_t j = 0; j < n - 1; j++) {
    for (size_t i = j + 1; i < n; i++) {
      if (fabs(U[j][j]) < tolerance) {
        std::cout << "Near-zero pivot element" << std::endl;
        break;
      }
      L[i][j] = U[i][j] / U[j][j]; // Multipliers
      for (size_t k = 0; k < n; k++) {
        U[i][k] = U[i][k] - L[i][j] * U[j][k]; // Row reduction
      }
    }
  }
}
