#%%
import numpy as np
import matplotlib.pyplot as plt
from utils import *
# %%
func = lambda x, y: x**2 + 2*y**2 + 4*x + y + 6
func = lambda x, y: 100*(y-x**2)**2 + (1-x)**2
plot_coutour(func, box = (-2,2), scale='log');

# %%
plot_surface_2d(func, box=(-2,2), azim=-60, elev=30, scale='log');

# %%

h = 1e-6
def numpartialx(f):
    return lambda x, y: (f(x+h, y)-f(x, y))/h

def numpartialy(f):
    return lambda x, y: (f(x, y+h)-f(x, y))/h

def grad_descent(f, x0 = (0,0), eta=0.01, num_steps=200):
    # if we do not give x0 any value, then by default it is (0,0)
    # starting at some point
    x, y = x0[0], x0[1]

    x_vals = np.zeros(num_steps)
    y_vals = np.zeros(num_steps)
    f_vals = np.zeros(num_steps)

    for i in range(num_steps):
        # update x and y
        # numerical gradient
        dx, dy = numpartialx(f)(x,y), numpartialy(f)(x,y)
        x = x - eta*dx
        y = y - eta*dy

        # let's store the x, y and f(x,y) values for later use
        x_vals[i] = x
        y_vals[i] = y
        f_vals[i] = f(x, y)
    
    return x_vals, y_vals, f_vals

#%%
num_steps = 1000
x_vals, y_vals, f_vals = grad_descent(func, x0 = (-2,2), eta = 1e-3, num_steps = num_steps)
print("The value of f(x,y): ", f_vals[-1], "after", 
      num_steps, "iterations at point", (x_vals[-1],y_vals[-1]))
plt.plot(f_vals)
plt.show()
# %%
plot_gradient_descent(func, x_vals, y_vals, step=50, scale='log')
# %%
