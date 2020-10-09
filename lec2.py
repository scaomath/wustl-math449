#%%
import numpy as np
# %%
a = np.array([3, 1, 9])
A = np.array([ [2, 4], [1, 3] ])
# %% colon syntax, slicing
# (start index):(end index, but exclusive):(step, default =1, optional)
arr = np.arange(10) + 2
print(f"The array is {arr}")
# %%
print(f"The first 3 entries: {arr[:3]}")
print(f"The last 3 entries: {arr[-3:]}")
print('The last 3 entries', arr[10-3: 10]) # 10 is the length of arr
print('The last 3 entries', arr[7], arr[8], arr[9])
# %% tridiagonal matrix diagonal = 2, -1 in the diagonal 1 from the main diagonal
A = np.diag([2,2,2,2,2]).astype(float)
A += np.diag([-1,-1,-1,-1], k=-1).astype(float)
A += np.diag(-np.ones((4,), dtype=float), k=1)

# %% generate a problem of Ax = b
# however, * is not matrix multiplication
arr1 = np.array([1, 2])
arr2 = np.array([3, 0.5])
# print(arr1*arr2)

# * is element-wise multiplication
arr3 = np.array([[10, 1], [0.5, 0.3]])
print(arr3*arr1)
# %% @ is the matrix-matrix or matrix-vector multiplication
# or we use a function called np.matmul()
vec1 = np.matmul(arr3, arr1) # arr1 is treated as a column vector
print(arr3@arr1) # only in Python 3
# %% toy model of Ax = b
# choose an x , generate a true solution
x_star = np.array([-2, 10, 3, 1, 3])
b = A@x_star
# %% Jacobi
# retrieve the diagonal entries
d = []
for i in range(A.shape[0]):
    d.append(1/A[i,i])

Dinv = np.diag(d)

# off diagonal entries L = lower triangular part of -A
L = np.zeros_like(A)
for i in range(1,5):
    for j in range(0,i):
        # print(i, j, A[i,j])
        L[i,j] = -A[i,j]

U = np.zeros_like(A)
for i in range(0,4):
    for j in range(i+1,5):
        U[i,j] = -A[i,j]

# %% 
print(np.tril(A, k=-1))
print(np.triu(A, k=1))
# %%
x = np.zeros_like(b)
for k in range(100):
    # x = Dinv times (L+U) times x + Dinv times b
    x = (Dinv@(L+U))@x + Dinv@b
    print(np.max(x-x_star))
# %%
