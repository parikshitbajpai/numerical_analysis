import numpy as np
import time                                         # For timing
import scipy
import math
import matplotlib.pyplot as plt
from limit import limit
from taylor import taylor


ntrials = 30

tolerance = 1e-12
x = 1

wtime = np.zeros((ntrials,3))
error_rel = np.zeros((ntrials,3))

for k in range(0,ntrials):
    start_limit = time.time()
    y_limit = limit(x,tolerance)
    end_limit = time.time() - start_limit

    start_taylor = time.time()
    y_taylor = taylor(x,tolerance)
    end_taylor = time.time() - start_taylor

    y_true = np.exp(x)

    wtime[k,0] = x
    wtime[k,1] = end_limit
    wtime[k,2] = end_taylor

    error_rel[k,0] = x
    error_rel[k,1] = abs(y_limit - y_true)/abs(y_true)
    error_rel[k,2] = abs(y_taylor - y_true)/abs(y_true)

    x += 2

plt.loglog(wtime[:,0],wtime[:,1],'-o',wtime[:,0],wtime[:,2],'-o',)
plt.title('Computation time vs. matrix size')
plt.legend(('Wall Time: Limit','Wall Time: Taylor'))
plt.show()

plt.loglog(error_rel[:,0],error_rel[:,1],'-o',error_rel[:,0],error_rel[:,2],'-o',)
plt.title('Computation time vs. matrix size')
plt.legend(('Error: Limit','Error: Taylor'))
plt.show()
