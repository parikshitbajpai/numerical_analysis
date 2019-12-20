# Multiplication of a given vector v by the preconditioned Jacobian. If F(u)=0 then J=DF is the Jacobian and the
# pre-conditioning is done by P=sqrt(nu) L where L L^t = -D^(2). The linear system is 
# P^(-1) J P^(-t) P^t du = - P^(-1) F. The dissipative term is then P^(-1) (-nu D^(2)) P^(-t) = L^(-1) (L L^t) L^(-t) = I.
# By L. van Veen, 2019 OnTechU. 
import numpy as np
from mult_by_Pinv import mult_by_Pinv
from mult_by_PTinv import mult_by_PTinv
from mult_by_J import mult_by_J

def mult_by_A(v,u,x0,x1,L,R,N,nu):
    # First multiply by P^(-t).
    w = mult_by_PTinv(v,x0,x1,N,nu)
    # Multiply by J.
    w = mult_by_J(w,u,x0,x1,L,R,N,nu)
    # Multiply by P^(-1).
    w =  mult_by_Pinv(w,x0,x1,N,nu)
    return w
