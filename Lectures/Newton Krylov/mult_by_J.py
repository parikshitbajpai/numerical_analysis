import numpy as np

def mult_by_J(v,u,x0,x1,L,R,N,nu):
    # Computes w = J v without forming J.
    w = np.zeros((N,1))
    h = (x1 - x0) / float(N + 1)

    # First dissipative term - nu D^(2) v.
    w[0] = nu * ( 2.0 * v[0] - v[1] ) / (h**2)
    for i in range(1,N-1):
        w[i] = nu * ( -v[i-1] + 2.0 * v[i] -v[i+1] ) / (h**2)
    w[N-1] = nu * ( -v[N-2] + 2.0 * v[N-1] ) / (h**2)

    # Now the advective terms: v * (D^(1) u) + u * (D^(1) v).
    w[0] += v[0] * u[1] / (2.0 * h) + u[0] * v[1] / (2.0 * h)
    for i in range(1,N-1):
        w[i] += v[i] * (u[i+1] - u[i-1]) / (2.0 * h) + u[i] * (v[i+1] - v[i-1]) / (2.0 * h)
    w[N-1] -= v[N-1] * u[N-2] / (2.0 * h) + u[N-1] * v[N-2] / (2.0 * h)
    
    # Finally terms stemming from the BC.
    w[0] -= L * v[0] / (2.0 * h)
    w[N-1] += R * v[N-1] / (2.0 * h)

    return w
