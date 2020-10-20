#%%
import numpy as np
# %% minesweeper game
matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

matrix_padded = [[False, False, False, False, False],
                 [False, True, False, False, False],
                 [False, False, True, False,False],
                 [False, False, False, False,False],
                 [False, False, False, False, False],]
matrix = np.array(matrix)
matrix_padded = np.zeros((matrix.shape[0]+2, matrix.shape[1]+2), dtype=bool)
matrix_padded[1:-1, 1:-1] = matrix
count = np.zeros_like(matrix, dtype=int)
# %%
# indicator = np.zeros_like(matrix, dtype=int)
for row_idx in range(1, matrix.shape[0]+1):
    for col_idx in range(1, matrix.shape[1]+1):
        count[row_idx-1, col_idx-1] = matrix_padded[row_idx-1:row_idx+2, col_idx-1:col_idx+2].sum()
        count[row_idx-1, col_idx-1] -= matrix_padded[row_idx,col_idx]
# %%
r = []
matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]
for i in range(len(matrix)):
    r.append([])
    print(r)
    for j in range(len(matrix[0])):
        l = -matrix[i][j]
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if 0<=i+x<len(matrix) and 0<=j+y<len(matrix[0]):
                    l += matrix[i+x][j+y]

        r[i].append(l)
# %% replace alphabet
list_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']
dict_replace = dict()
for i, a in enumerate(list_alpha):
    if i == len(list_alpha)-1: 
        break
    dict_replace[a] = list_alpha[i+1]
# %%
inputString = "crazy"
lst = [s for s in inputString]
for pos, s in enumerate(lst):
    lst[pos] = dict_replace[s]
# %%
for i in inputString:
    print(chr((ord(i)-96)%26+97))

# %%
