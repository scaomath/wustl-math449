#%%
import numpy as np
import matplotlib.pyplot as plt
#%%

def f(x):
    '''
    The function f(x)
    '''
    a = 2
    return x**3-a

def df(x):
    '''
    The derivative of f(x)
    '''
    return 3*x**2

def newtonArray(f, df, x0, n):
    '''
    Replace the pass with the code, try replacing Newton's method with a simple relaxation.
    '''
    pass

def plotError(y, x):
    '''
    Plot the error using matplotlib
    '''
    err = y - x
    plt.semilogy(np.abs(err))
    plt.show() 

def main():
    n = 20
    x0 = 1
    x = newtonArray(f, df, x0, n)
    y = 2**(1/3)
    plotError(y,x)

#%%
if __name__ == "__main__":
    main()
