#%%
import numpy as np
# %%
mat1 = [[0, 1, 1, 2], 
        [0, 5, 0, 0], 
        [2, 0, 3, 3]]
# mat1 = np.array(mat1)
print(mat1)
sumMat = 0
for i in range(len(mat1[0])):
    for j in range(len(mat1)):
        print(f"Checking {(j+1,i+1)}-th entry.")
        if mat1[j][i] == 0:
            break
        else:
            sumMat += mat1[j][i]
            print(f"sum is {sumMat}")

# %%
def allLongestStrings(inputArray):
    import numpy as np
    arr = np.array(inputArray)
    strLen = [len(s) for s in inputArray]
    arr_tmp = arr[strLen == max(strLen)]
    return list(arr_tmp)

# %%
arr = ["aba", 
 "aa", 
 "ad", 
 "vcd", 
 "aba"]
arr = np.array(arr)
strLen = [len(s) for s in arr]
arr_tmp = arr[strLen == np.ones(len(arr))*max(strLen)]
# %%
