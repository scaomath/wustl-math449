#%% coding lecture no.3 on linear solver
from homework.hw2 import *
import numpy as np
from numpy.linalg import norm
# %% compressed sparse row or csr
A = getMatrix(n=5)
# generate a random vector as the solution 
x_true = np.random.randn(5)
b = A@x_true
# %% 
# D is an array
D, L, U = getAuxMatrix(A)

numIter = 200 # total number of iterations
nDim = A.shape[0]
x = np.zeros((numIter+1, nDim))
# x[0] = np.zeros((nDim, ))
for k in range(numIter):
    # diagonal matrix (matrix multiplication) vector 
    # = diagonal entry vector * vector elementwisely
    # D is a vector representing the diagonal entries
    x[k+1] = ((L+U)@x[k])/D + b/D
    if k % 10 is 0:
        # 1.0 after 80ish iteration is because
        # we have reached error of machine epsilon level
        print(norm(x[k+1] - x_true)/norm(x[k] - x_true) )

# %%
# plotConvergence(x_true, x[:10], scale='linear')
# %%
def jacobiIteration(A, b, x0=None, tol=1e-13, numIter=100):
    '''
    Jacobi iteraiton:
    A: nxn matrix
    b: (n,) vector
    x0: initial guess
    numIter: total number of iteration
    tol: algorithm stops if ||x^{k+1} - x^{k}|| < tol
    return: x
    x: solution array such that x[i] = i-th iterate
    '''
    n = A.shape[0]
    x = np.zeros((numIter+1, n))
    if x0 is not None:
        x[0] = x0
    D, L, U = getAuxMatrix(A)
    for k in range(numIter):
        x[k+1] = ((L+U)@x[k])/D + b/D
        if norm(x[k+1] - x[k]) < tol:
            break
    
    return x[:k+1]

x = jacobiIteration(A, b)

# %% What happens if we increase problem size
# 10x10 matrix
A = getMatrix(n=20)
x_true = np.random.randn(20)
b = A@x_true

## number of iterations needed is approximately O(n^2)
x = jacobiIteration(A, b, numIter = 2000)



# %%
