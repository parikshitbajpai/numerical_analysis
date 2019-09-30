//* This file is part of the LU decomposition program
//* Written for MCSC 6020G - Numerical Analysis (Fall 2019)
//*
//* Author - Parikshit Bajpai

#pragma once

class LU {
private:
  float tolerance;

public:
  void LU(float &matrix[][]);
}
