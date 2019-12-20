# optimize of Newton-hook. Programmed in lectures 13 -- ...
import numpy as np
from copy import copy
from Newton import Newton

def optimize(x,dx,f,df,delta):
    N = np.shape(x)[0]
    J = df(x)
    U,S,Vt = np.linalg.svd(J)
    print('min sig=%e' % (np.min(S)))
    r = f(x)
    g = U.T @ r
    lm = Newton(delta,g,S)
    w = np.zeros((N,1))
    for i in range(N):
        w[i] = -S[i] * g[i] / (S[i]**2 + lm)
    dx = Vt.T @ w
    return dx
