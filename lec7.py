#%%
import numpy as np
import matplotlib.pyplot as plt
from utils import *
# %%
'''
n is the number of interior points for a finite difference matrix
'''
n = 40
I = np.diag(np.ones(n)) 
A = 2*I - np.diag(np.ones(n-1), k=1) -  np.diag(np.ones(n-1), k=-1)
# %% b = zero vector
x = np.random.randn(n)
r = -A@x
p = r
maxIter = 10000
tol = 1e-4
k = 0
# %% converges in O(n) steps
# Jacobi converges in O(n^2) steps
while np.linalg.norm(r)>tol and k < maxIter:
    alpha = r@r/(p@(A@p))
    x = x + alpha*p
    tmp = r@r # r_k dot with r_k 
    r = r - alpha*(A@p)
    p = r + (r@r)/tmp*p
    k += 1