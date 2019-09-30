#include "LU.h"
#include <iostream>
#include <math.h>
#include <stdio.h>

int main(int argc, char const *argv[]) {
  float A[3][3] = {{2, -1, -2}, {-4, 6, 3}, {-4, -2, 8}};
  LU(A);
  return 0;
}
