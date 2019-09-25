import numpy as np
import time                              # For timing
import matplotlib.pyplot as plt          # For plotting
from LUP import LUP

ntrials = 8                                   # nr. of trials
wtime=np.zeros((ntrials,2))                
accuracy = np.zeros((ntrials,3))
n=4
for k in range(0,ntrials):
    A = np.random.rand(n,n)
    start=time.time()                    # Get start time
    L,U,P,par = LUP(A)
    elapsed=time.time()-start            # Measure elapsed time
    check = np.linalg.norm(np.matmul(L,U)-np.matmul(P,A))
    condition = np.linalg.cond(A,2)
    print('n = %d, error = %e, K(A) = %e' % (n,check,condition))
    n *= 2
    wtime[k,0] = n
    wtime[k,1] = elapsed
    accuracy[k,0] = n
    accuracy[k,1] = check
    accuracy[k,2] = condition
print(wtime)
plt.loglog(wtime[:,0],wtime[:,1],'-*')
plt.show()
plt.loglog(accuracy[:,0],accuracy[:,1],'-r')
plt.loglog(accuracy[:,0],accuracy[:,2],'-k')
plt.show()

