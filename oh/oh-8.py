#%% 
import numpy as np
import math

from torch import dtype
# %%
'''
Given two cells on the standard chess board, determine whether they have the same color or not.
'''
cell1 = "A1"
cell2 = "B2"

print(not (ord(cell1[0]) - ord(cell2[0]))%2 )
# %%
'''
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.
'''
n = 10
firstNumber = 2
if firstNumber < n//2:
    output = firstNumber+n//2
else:
    output = firstNumber-n//2
# %%
a = np.array([2,3], dtype=int)
a = np.array([2, 4, 7, 8])
# %%
'''
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.
'''
#%%
inputArray = ["abc", 
 "abx", 
 "axx", 
 "abx", 
 "abc"]
inputArray = sorted(inputArray)
indicator = []
for i in range(len(inputArray)-1):
    s1 = inputArray[i]
    s2 = inputArray[i+1]
    lst1 = sorted([s for s in s1])
    lst2 = sorted([s for s in s2])
    ind_ = [lst1[i]!=lst2[i] for i in range(len(lst1))]
    ind_ = sum(ind_)
    indicator.append(ind_)
    break
# %%
def stringsRearrangement(inputArray):
    import itertools
    allArray = list(itertools.permutations(inputArray))
    allInd = []
    for arr in allArray:
        indicator = []
        for i in range(len(arr)-1):
            s1 = arr[i]
            s2 = arr[i+1]
            lst1 = [s for s in s1]
            lst2 = [s for s in s2]
            ind_ = [lst1[i]!=lst2[i] for i in range(len(lst1))]
            ind_ = sum(ind_)
            indicator.append(ind_)
            
        allInd.append(all([i==1 for i in indicator]))
    return bool(sum(allInd))