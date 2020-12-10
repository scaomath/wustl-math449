#%%
import numpy as np
# %%
def getMatrix(n=20):
    I = np.diag(np.ones(n)) 
    A = 2*I - np.diag(np.ones(n-1), k=1) -  np.diag(np.ones(n-1), k=-1)
    return A

def powerIter(A, x=None, maxIter=1000, tol=1e-8):
    err = tol + 1
    n = A.shape[0]
    if x is None:
        x = np.ones(n)
    lambda_h = [] # empty list
    k = 0
    while err >= tol:
        y = A@x
        tmp1 = y.dot(x)
        tmp2 = x.dot(x)
        y = y/np.linalg.norm(y)
        err = np.linalg.norm(x - y)
        x = y
        lambda_h.append(tmp1/tmp2)
        k += 1
        if k > maxIter:
            break
    return lambda_h

def main():
    A = getMatrix(n=40)
    lambda_h = powerIter(A)
    print(lambda_h[-5:])
#%%
if __name__ == "__main__":
    main()
