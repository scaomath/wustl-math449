#%%
import numpy as np
import matplotlib.pyplot as plt
from utils import *
# %%
# f = lambda x,y: x**2 + 2*y**2 + 4*x + y + 6
f = lambda x,y: 100*(y-x**2)**2 + (1-x)**2 # Rosenbrock
# print(f(0., 2))
# %%
plot_coutour(f, box=(-2,2), scale='log')
#%%
plot_surface_2d(f, box=(-2,2),scale='log');
# %%
h = 1e-8
gradhx = lambda x,y: (f(x+h, y) - f(x,y))/h
gradhy = lambda x,y: (f(x, y+h) - f(x,y))/h

print(gradhx(0,0), gradhy(0,0))
# %% gradient descent
'''
Is bigger step size better and converges faster?
A partially yes.
'''
eta = 1e-6 # step size (learning rate) cannot be too big
x0 = np.array([6,7]) # initial guess
N = 5000 # max iter

# keeping track of x, y at each iteration
xvals = np.zeros(N)
yvals = np.zeros(N)
fvals = np.zeros(N)

xvals[0] = x0[0]
yvals[0] = x0[1]
fvals[0] = f(xvals[0], yvals[0])

for k in range(N-1):
    '''
    next iterate x_{k+1} = x_k - eta* grad f(x_k) 
    '''
    xvals[k+1] = xvals[k] - eta*gradhx(xvals[k], yvals[k])
    yvals[k+1] = yvals[k] - eta*gradhy(xvals[k], yvals[k])
    fvals[k+1] = f(xvals[k+1], yvals[k+1])

# %%
plt.semilogy(fvals[:1000])
# plt.semilogy(np.arange(20), fvals[:20])
# %%
plot_gradient_descent(f, xvals, yvals, scale='log', step=200)
# %%
