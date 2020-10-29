#%% Office hour Oct 29
import numpy as np
from time import time
import json
# %%
'''
Given array of integers, remove each kth element from it.
'''
inputArray = [1, 2, 3, 4, 5, 3, 7, 30, 3, 10] 
outArray = [s for i, s in enumerate(inputArray) if (i+1)%7]
print(outArray)
# %%
'''
Find the leftmost digit that occurs in a given string.
'''
inputString = "q2q-q"
print([s.isdigit() for s in inputString])
#%%
'''
Given array of integers, find the maximum possible sum of some of its k consecutive elements.
number of sums = len(inputArray) - k + 1
last element in the array starting the sum is len(inputArray) - k
'''

with open('test-20.json') as f:
    data = json.load(f)
inputArray = data['input']['inputArray']
k = data['input']['k']
#%%
# inputArray = inputArray[:70000]
t = time()
n = len(inputArray) - k + 1
sumArray = [sum(inputArray[i:i+k]) for i in range(n)]
m = max(sumArray)
print(time()-t)
# %%
arr = np.array(inputArray)
t = time()
# for i in range(10):
#     sum(arr[i:i+k])
sorted(arr)
t1 = time()
print(t1-t)
# %%
def max_subarray(inputArray,k):
    """Find the largest sum of any contiguous k-subarray."""
    best_sum = 0  # or: float('-inf')
    current_sum = sum(inputArray[:k])
    for i in range(k, len(inputArray)):
        current_sum = current_sum + inputArray[i] - inputArray[i-k]
        best_sum = max(best_sum, current_sum)
    return best_sum

t = time()
# best_sum = max_subarray(inputArray,k)
best_sum = max_subarray([2, 3, 5, 1, 6], 2)
print(time()-t)
# %%
