#%% The sample codes in coding lecture 1
import numpy as np

#%%
# print(" Welcome to Math 449 first online session. ")

# comment uncomment Ctrl/Cmd + /

print(2**(5/3))
# %% Variable and list
'''
x_{k+1} = g(x_{k})
'''
# %%
a = [1, 2, 4, 8]
print(a[0]) # Python's index starts from 0
print(a[0:2]) 
print(a[2])
print(a[:2]) # same with print(a[0:2]) 
# i:j access to a[i] to a[j] (non-inclusive)
# :j acess to starting to a[j] (non-inclusive)
# %%
b = [1, 100, 2.4, 1.3, 3]
print(b[2:]) # prints b[2] to the end of b
# %% Range
for i in range(5): # range() is called an iterable
    print(i)
# %% iterative method
# x_{k+1} = x_k - f(x_k)/f'(x_k)
# try this with f(x) = x^2 - 2
x0 = 1
x = x0
n = 100 # number of iterations
for i in range(n):
    a = (x**2 - 2)/(2*x)
    x -= a # x = x-a
print(x)

# %% 
arr = np.arange(10) # numpy's range
print(arr)
arr1 = np.zeros(10)
print(arr1)
print(type(arr1))
# %%
n = 20
x = np.zeros(n+1) # n = number of iterations

x[0] = 1 # initial guess
for k in range(n):
    x[k+1] = x[k] - (x[k]**2 - 2)/ (2*x[k])

# %% Visualization
# plot 
import matplotlib.pyplot as plt
plt.plot(np.abs(x-np.sqrt(2)))
