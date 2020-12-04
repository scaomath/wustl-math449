#%% Power method lecture
import numpy as np
import matplotlib.pyplot as plt
# %%
'''
n is the number of interior points for a finite difference matrix
'''
n = 10
I = np.diag(np.ones(n)) 
A = 2*I - np.diag(np.ones(n-1), k=1) -  np.diag(np.ones(n-1), k=-1)
print(A)
T = I - A/2 # T is the matrix in the Jacobi iteration D^{-1}(L+U)

# %%
tol = 1e-4
err = tol + 1
x = np.ones(10)
lambda_h = [] # empty list
k = 0
while err >= tol:
    y = T@x
    tmp1 = y.dot(x)
    tmp2 = x.dot(x)
    y = y/np.linalg.norm(y)
    err = np.linalg.norm(x - y)
    x = y
    lambda_h.append(tmp1/tmp2)
    k += 1
    if k > 10000:
        break

# %% plot the eigenvalue approximation of lambda
'''
True lambda of the biggest magnitude is cos(pi*h) = cos(pi/(n+1))
of the Jacobi iteration
'''
lambda_h = np.array(lambda_h)
lambda_ = np.cos(np.pi/(n+1)) 
plt.figure(1)
plt.plot(lambda_*np.ones(len(lambda_h)))
plt.plot(lambda_h)

plt.figure(2) # show the error in log scale
plt.semilogy(np.abs(lambda_ - lambda_h))
plt.show()
# %%
