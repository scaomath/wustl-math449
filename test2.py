#%%
import numpy as np # import numpy module as np in namespace
from homework.hw1 import * # import hw1.py
# %%
x = np.array([1, 5, 10, 2])

print(x.reshape(2,2)) # object oriented
print(x.shape)
# %%

# %%
newtonArray(f, df, 1)
# %% when f'(xi) = 0

def f(x):
    '''
    f(0)=0
    '''
    return np.exp(x) - x - 1

def df(x):
    '''
    f'(0)=0
    '''
    return np.exp(x) - 1
# %%
x_val = newtonArray(f, df, 40)
x_val = x_val[x_val!=0]
# %%
import matplotlib.pyplot as plt
# %%
plt.semilogy(x_val)
# conclusion: initial convergence is sublinear
# when sufficiently close, linear convergence
# %%
