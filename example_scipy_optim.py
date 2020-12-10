#%%
import numpy as np
from utils import *
import scipy
import scipy.optimize as optimize
# %%
'''
Rosenbrock function
'''
func = lambda x, y: 100*(y-x**2)**2 + (1-x)**2
plot_coutour(func, box = (-2,2), scale='log');
# %%
'''
Source of scipy.optimize.minimize
https://github.com/scipy/scipy/blob/v1.5.4/scipy/optimize/_minimize.py#L44-L644
outputs = minimize(fun, x0, args=(), method=None, jac=None, hess=None,
             hessp=None, bounds=None, constraints=(), tol=None,
             callback=None, options=None)

fun : callable
x0 : ndarray, shape (n,)

jac{callable, ‘2-point’, ‘3-point’, ‘cs’, bool}, optional

Method for computing the gradient vector. Only for CG, BFGS, Newton-CG, L-BFGS-B, TNC, SLSQP, dogleg, trust-ncg, trust-krylov, trust-exact and trust-constr. If it is a callable, it should be a function that returns the gradient vector:

jac(x, *args) -> array_like, shape (n,)

hess{callable, ‘2-point’, ‘3-point’, ‘cs’, HessianUpdateStrategy}, optional
Method for computing the Hessian matrix. Only for Newton-CG, dogleg, trust-ncg, trust-krylov, trust-exact and trust-constr. If it is callable, it should return the Hessian matrix:

hess(x, *args) -> {LinearOperator, spmatrix, array}, (n, n)

LinearOperator: https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.LinearOperator.html
spmatrix: https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.spmatrix.html?highlight=spmatrix#scipy.sparse.spmatrix
'''
# %%
def rosenbrock(x):
    """The Rosenbrock function in n-dimension"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 \
               + (1-x[:-1])**2.0)

def rosenbrock_grad(x):
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    grad = np.zeros_like(x)
    grad[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
    grad[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    grad[-1] = 200*(x[-1]-x[-2]**2)
    return grad

#%%
results = optimize.minimize(rosenbrock, 
                            x0=[4, 4], method='Newton-CG', 
                            jac=rosenbrock_grad, 
                            options={'xtol': 1e-6,  'disp': True}, 
                            callback=print)

# %% adding a customized callback
def callback_func(x):
    global num_f_vals, x_vals
    print(f'{num_f_vals:4d}   {x[0]: 3.6f}   {x[1]: 3.6f}')
    num_f_vals += 1
    x_vals = np.append(x_vals, [x], axis=0)

num_f_vals=0
x_vals = np.array([[4,4]])

results = optimize.minimize(rosenbrock, x0=x_vals, method='Newton-CG', 
               jac=rosenbrock_grad, 
               options={'xtol': 1e-6, 'disp': True}, 
               callback=callback_func)
#%%
plot_gradient_descent(func, x_vals[:,0], x_vals[:,1], box=(-3,3), step=10, scale='log', alpha =0.4)
# %%
