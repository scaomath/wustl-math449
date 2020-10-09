#%% Office hour Oct 6
import numpy as np
#%%
a = [-1, 150, 190, 170, -1, -1, 160, 180]
#%%
def sortByHeight(a):
    '''
    Step 1: retrive tree's locations (-1)
    Step 2: sort the rest
    Step 3: keep the indices of the non-trees, numpy slicing for the final output
    '''
    a = np.array(a)
    idxHeights = np.where(a!=-1)
    a[idxHeights[0]] = np.sort(a[idxHeights[0]])    
    return a
#%%
a = np.array(a)
idxHeights = np.where(a!=-1)
a[idxHeights[0]] = np.sort(a[idxHeights[0]])
print(a)
#%%
def reverseNonNestedParentheses(inputString):
    import numpy as np
    arrStr = np.array([s for s in inputString])
    idxLeft = np.where(arrStr == '(')[0]
    idxRight = np.where(arrStr == ')')[0]
    for n in range(len(idxLeft)):
        arrMid = arrStr[idxLeft[n]+1: idxRight[n]]
        arrStr[idxLeft[n]+1: idxRight[n]] = arrMid[::-1]

    outStr = [s for s in arrStr if s != '(' and s != ')']
    return "".join(s for s in outStr)

def reverseInParentheses(inputString):
    import numpy as np
    arrStr = np.array([s for s in inputString])
    idxLeft = np.where(arrStr == '(')[0]
    idxRight = np.where(arrStr == ')')[0]
    while idxLeft[-1] + 1 < idxRight[0] and len(idxLeft) >=2:
        arrMid = arrStr[idxLeft[-1]+1: idxRight[0]]
        arrStr[idxLeft[-1]+1: idxRight[0]] = arrMid[::-1]
        arrStr_new = np.zeros((len(arrStr)-2,), dtype=str)
        arrStr_new[:idxLeft[-1]] = arrStr[:idxLeft[-1]]
        arrStr_new[idxLeft[-1]:idxRight[0]-1] = arrMid[::-1]
        arrStr_new[idxRight[0]-1:] = arrStr[idxRight[0]+1:]
        idxLeft = np.where(arrStr_new == '(')[0]
        idxRight = np.where(arrStr_new == ')')[0]
        arrStr = arrStr_new
    outString = "".join(s for s in arrStr)
    return reverseNonNestedParentheses(outString)
# %%
inputString = "foo(bar)baz(blim)"
# %%
arrStr = np.array([s for s in inputString])
print(arrStr)
idxLeft = np.where(arrStr == '(')[0]
idxRight = np.where(arrStr == ')')[0]
while idxLeft[-1] < idxRight[0]:
    arrMid = arrStr[idxLeft[-1]+1: idxRight[0]]
    arrStr[idxLeft[-1]+1: idxRight[0]] = arrMid[::-1]
    idxLeft = np.where(arrStr == '(')[0]
    idxRight = np.where(arrStr == ')')[0]
    print(arrStr)

for n in range(len(idxLeft)):
    arrMid = arrStr[idxLeft[n]+1: idxRight[n]]
    arrStr[idxLeft[n]+1: idxRight[n]] = arrMid[::-1]
    print(arrStr)

outStr = [s for s in arrStr if s != '(' and s != ')']
print(outStr)
print("".join(s for s in outStr))
# %%
# %%
# inputString = "(foo)"
# inputString = "foo(bar(b(zab)az))blim(bar)"
inputString = "foo(bar(b(zab)az))blim"
# inputString = "foo(bar)baz(blim)"
arrStr = np.array([s for s in inputString])
idxLeft = np.where(arrStr == '(')[0]
idxRight = np.where(arrStr == ')')[0]
k = 0
while idxLeft[-1] + 1 < idxRight[0] and len(idxLeft) >=2:
    print(k)
    arrMid = arrStr[idxLeft[-1]+1: idxRight[0]]
    print(arrStr)
    print(arrMid)
    # arrStr[idxLeft[-1]+1: idxRight[0]] = arrMid[::-1]
    arrStr_new = np.zeros((len(arrStr)-2,), dtype=str)
    arrStr_new[:idxLeft[-1]] = arrStr[:idxLeft[-1]]
    arrStr_new[idxLeft[-1]:idxRight[0]-1] = arrMid[::-1]
    arrStr_new[idxRight[0]-1:] = arrStr[idxRight[0]+1:]
    
    print(arrStr_new)
    print()
    idxLeft = np.where(arrStr_new == '(')[0]
    idxRight = np.where(arrStr_new == ')')[0]
    arrStr = arrStr_new
    k += 1
    # # print(arrStr)
    # if k >= 1: break

reverseNonNestedParentheses(arrStr)
# %%
def reverseInParentheses(inputString):
    while('(' in inputString):
        # str.find(substr, (start, (end)))
        leftP = inputString.rfind('(')
        rightP = inputString.find(')',leftP)

        # reverse string by [ end : start : -1 ]
        inputString = inputString[:leftP] \
            + inputString[rightP-1:leftP:-1] \
                + inputString[rightP+1:]

    return inputString

#%%
from scipy.optimize import minimize
a= [-1.5, 0.5]
b= [1.5, 1.5]
v1= 4.4
v2= 1.1
timefunc = lambda y: ((y-a[1])**2 + a[0]**2)**0.5/v1 \
                    + ((y-b[1])**2 + b[0]**2)**0.5/v2
res = minimize(timefunc, (a[1]+b[1])/2)

