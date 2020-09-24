#%%
import json
import numpy as np
import time
#%%
# def increasingSequence(sequence):
#     ind = 1
#     for n in range(len(sequence)-1):
#         ind *= (sequence[n+1] > sequence[n])
#     return bool(ind) 


# def almostIncreasingSequence(sequence):
#     ind = False
#     for n in range(len(sequence)):
#         tmp = sequence[0:n]+sequence[n+1:]
#         ind = increasingSequence(tmp) or ind
#     return bool(ind)

def almostIncreasingSequence(s):
    import numpy as np
    ind1 = [(s[i]>=s[i+1]) for i in range(len(s)-1)]
    tmp = np.arange(len(s)-1)
    ind2 = sum(ind1)
    ind5 = 1
    if ind2 == 1:
        tmp2 = tmp[ind1]
        ind3 = tmp2[0]+1
        s = s[:ind3]+ s[ind3+1:]
        ind4 = np.array([(s[i]>=s[i+1]) for i in range(len(s)-1)])
        ind5 = sum(ind4)
    ind6 = (ind2 <= 1) and (ind5==0)
    
    return ind6

    
# %%
print(almostIncreasingSequence([3, 5, 67, 98, 3]))
print(almostIncreasingSequence([1,2,1,2]))
print(almostIncreasingSequence([1,3,2]))
# %%
# s = [3, 5, 67, 98, 3]
s = [1,2,1,2]
for n in range(len(s)):
    tmp = s[:n] + s[n+1:]
    print(f"n is {n}, s is {tmp}")

#%% 
[i for i in range(10)]
#%%
s = [1,2,1,2]
ind1 = [(s[i]>=s[i+1]) for i in range(len(s)-1)]
tmp = np.arange(len(s)-1)
ind2 = sum(ind1)
ind5 = 1
if ind2 == 1:
    tmp2 = tmp[ind1]
    ind3 = tmp2[0]+1
    s = s[:ind3]+ s[ind3+1:]
    ind4 = [(s[i]>=s[i+1]) for i in range(len(s)-1)]
    ind5 = sum(ind4)
ind6 = (ind2 <= 1) and (ind5==0)
print(ind6)

#%%
with open('test-35.json') as f:
  data = json.load(f)
s = data['input']['sequence']
print(f"length of s: {len(s)}")

# %%
t = time.time()
[i for i in range(len(s)-1) if (s[i]>=s[i+1])]
t_elapsed = time.time()-t
print(f"{t_elapsed} seconds to run this loop.")
# %%
def increasingSequence(s):
    tmp = [i for i in range(len(s)-1) if (s[i]>=s[i+1])]
    return not len(tmp), tmp

# def increasingSequence(s):
#     ind = [(s[i]>=s[i+1]) for i in range(len(s)-1)]
#     return not sum(ind)

# def almostIncreasingSequence(s):
#     ind = False
#     for n in range(len(s)):
#         tmp = s[0:n]+s[n+1:]
#         ind = increasingSequence(tmp) or ind
#     return ind

def almostIncreasingSequence(s):
    isIncreasing, idxDecreasing = increasingSequence(s)
    if isIncreasing: 
        return True
    elif len(idxDecreasing) > 1:
        return False
    elif len(idxDecreasing) == 1:
        idx1 = idxDecreasing[0]
        s_1 = s[0:idx1]+s[idx1+1:]
        s_2 = s[0:idx1+1]+s[idx1+2:]
        isIncreasing1, _ = increasingSequence(s_1)
        isIncreasing2, _ = increasingSequence(s_2)
        return isIncreasing1 or isIncreasing2



# %%
t = time.time()
almostIncreasingSequence(s[:1000])
t_elapsed = time.time() -t
print(f"{t_elapsed} seconds to run this loop.")


# %%
isIncreasing, idxDecreasing = increasingSequence(s)
