#%%
# from homework.hw2 import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import *
from numpy.linalg import norm

def getMatrix(n=10, isDiagDom=True):
    '''
    Return an nxn matrix which is the discretization matrix
    from finite difference for a diffusion problem.
    To visualize A: use plt.spy(A.toarray())
    '''
    # Representation of sparse matrix and right-hand side
    assert n >= 2
    n -= 1
    diagonal  = np.zeros(n+1)
    lower     = np.zeros(n)
    upper     = np.zeros(n)

    # Precompute sparse matrix
    if isDiagDom:
        diagonal[:] = 2 + 1/n**2
    else:
        diagonal[:] = 2
    lower[:] = -1  #1
    upper[:] = -1  #1
    # Insert boundary conditions
    # diagonal[0] = 1
    # upper[0] = 0
    # diagonal[n] = 1
    # lower[-1] = 0

    
    A = diags(
        diagonals=[diagonal, lower, upper],
        offsets=[0, -1, 1], shape=(n+1, n+1),
        format='csr')

    return A

def getAuxMatrix(A):
    '''
    return D, L, U matrices for Jacobi or Gauss-Seidel
    D: array
    L, U: matrices
    '''
    # m = A.shape[0]
    D = csr_matrix.diagonal(A)
    L = -tril(A, k=-1)
    U = -triu(A, k=1)
    return D, L, U
# %% plot a function y = sin(2*pi*x)/(2*pi)^2
PI = np.pi

def myfunc(x):
    return np.sin(2*PI*x)/(2*PI)**2

#lambda, like @(x) function in MATLAB
# y = lambda x: np.sin(2*PI*x)/(2*PI)**2
# %%
n_sample = 1000
x_sample = np.linspace(0, 1, num=n_sample)
y_sample = myfunc(x_sample)
plt.plot(x_sample, y_sample, label='True solution to the equation')
plt.legend()
# %% finite difference
'''
A has 2 on the diagonal, -1 on the off-diagonal
n: number of points
x: a vector representing x_0, x_1, x_2, ..., x_{n-1}, x_n
A: the finite difference matrix
f: f_j = f(x_j) for j= 1, 2, ..., n-1
b: right hand side h^2*f
'''
n = 10 # h= 1/n
x = np.linspace(0,1,num=n+1)
A = getMatrix(n = n-1, isDiagDom=False)
f_func = lambda x: np.sin(2*PI*x)
f = f_func(x[1:-1]) # x[1:-1] represents x_1 to x_{n-1}
b = f*(1/n)**2
# %% Apply Jacobi for Ay = f
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

numIter = 20
y = np.zeros((numIter, n+1))
y[:,1:-1] = jacobiIteration(A=A, b=b, numIter=numIter)

# %% plot what y is like (finite difference approximation)
for i in range(0, numIter, 5):
    plt.plot(x, y[i], label=f'Iterate at {i}-th iteration')
plt.plot(x_sample, y_sample, label='True solution to the equation')
plt.legend()
# %% record the error
'''
myfunc(x): y(x_j) where y is the true solution
y: y_j the finite difference approximation
'''
error = np.max(np.abs(myfunc(x)-y[-1]))
print(error)
# %%
