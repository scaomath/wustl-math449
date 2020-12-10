#%% 
import numpy as np
from utils import *
# %% 
'''
Implemention of Newton-CG from scratch for the Rosenbrock function
'''
func = lambda x, y: 100*(y-x**2)**2 + (1-x)**2
plot_coutour(func, box = (-2,2), scale='log');
# %%
def gradient_f(x):
    grad = np.zeros(2)
    grad[0] = -400 * (x[1] - x[0] * x[0]) * x[0] - 2 * (1 - x[0])
    grad[1] = 200 * (x[1] - x[0] * x[0])
    return grad

def hessian_f(x):
    Hess = np.zeros((2,2))
    Hess[0, 0] = 1200*x[0]**2 - 400*x[1] + 2
    Hess[0, 1] = -400*x[0]
    Hess[1, 0] = -400*x[0]
    Hess[1, 1] = 200
    return Hess
# %% 
tol = 1e-6
eta = 1e-1 # alpha in the outer loop
N = 1000 # outer iteration 
M = 10 # inner iteration CG
x = np.zeros((N+1,2))
x[0] = [-2,1] # initial guess
f_vals = np.zeros(N+1)
f_vals[0] = func(x[0,0], x[0,1]) #x[0,0] is x0's x, x[0,1] is x0's y
# %% Newton-CG
for k in range(N): # outer iteration
    z = np.array([0.,0.])
    r = gradient_f(x[k])
    d = -r
    B = hessian_f(x[k])
    for j in range(M): # inner iteration
        if (B@d)@d <= 0: 
            '''
            check if Hessian is negative at any direction in the current search space
            '''
            if j == 0:
                p = gradient_f(x[k])
            else:
                '''
                z is inner loop's search directions
                we update the overall search direction up to the previous inner iteration where
                the negative Hessian is obtained
                '''
                p = z
            '''
            jump out from the inner iteration and use -grad as the search direction
            '''
            break 

        '''
        the following resembles the regular CG
        '''
        alpha = r@r/((B@d)@d)
        z += alpha*d
        r_old = r
        r += alpha*(B@d)
        if np.linalg.norm(r) < tol: 
            '''
            stopping criterion of the inner iteration
            '''
            p = z
            break
        d = -r + r@r/(r_old@r_old)*d
    '''
    here p=z update the search direction if the stopping criterion of the inner iteration
    is not met and a maximum M iterations in the inner loops have been executed
    '''
    p = z
    x[k+1] = x[k] + eta*p
    f_vals[k+1] = func(x[k+1,0], x[k+1,1]) # update the function values

# %%
plot_gradient_descent(func, x[:,0], x[:,1], box=(-3,3), step=10, scale='log', alpha =0.4)
# %% 
plt.semilogy(f_vals) # almost linear convergence (shown in the log scale)
plt.show()
# %%
