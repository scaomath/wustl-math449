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
'''
Callback: 
1. function a (main, minimize functions) calls function b (objective function), and wants to make b run a specific independent task at some point during b's execution. 
2. We want to be able to vary which chunk of code gets called in different calls to b, so it cannot be hard-coded inside b (for examples, hard to give b what specific inputs needed). 
3. Solution is to introduce c (callback), to b, as one argument, and b uses that parameter c to call the functionality that a wants b to call. 
4. Function b may pass some parameters to the function represented by c, when it calls it. These could be either internally generated, passed from a, or a combination of both. So, by changing the value of the function c that gets passed to b (on different calls to b), a can change what chunk of code b calls.
5. We can passed different callbacks to a, we could enhance a in a different way, without changing the code of the a function itself. This leads to code with less coupling, which is generally preferable for modularity and maintainability.
'''
# %%
def report_progress(i, result):
    print(f"\nItems processed: {i}. Running result: {result}.\n")

def square(x):
    return x**2

def main(func, num_calls, report_interval, callback):
    '''
    a fancy way of computing sum of squares
    '''
    print(f"Entered main(): total number of calls = {num_calls}, report_interval = {report_interval}, callback = {callback.__name__}\n\n")
    result = 0
    print("Processing ...\n")
    for i in range(1, num_calls + 1):
        print(f'{i}-th call of the function {func.__name__}\n')
        result += func(i)
        if i % report_interval == 0:
            # This is the call to the callback function 
            # that was passed to this function.
            callback(i, result)
 
main(square, 12, 5, callback=report_progress) # no explicit input is given to report_progress

# %%
