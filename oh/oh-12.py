#%% oh-12
import numpy as np
# %%
votes = [2, 3, 1, 3, 4]
print(votes.count(3))
a = ['a', 'b','a','a', 's']
print(a.count('a'))
# %%
'''
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.
'''
#%%
inputString = "00-1B-63-84-45-E6"
splitStr = inputString.split('-')
lenStr = [len(s)==2 for s in splitStr]
# %%
def isMAC48Address(inputString):
    splitStr = inputString.split("-")
    lenStr = [len(s) !=2 for s in splitStr]
    if len(splitStr) != 6 or any(lenStr):
        return False
    else:
        isInputGood = [checkOrd(s) for s in splitStr]
        return all(isInputGood)
            
            
def checkOrd(s):
    '''s is a length 2 string'''
    isFirstGood = (48<= ord(s[0]) <= 57) or (65 <= ord(s[0]) <=70) 
    isSecondGood = (48<= ord(s[1]) <= 57) or (65 <= ord(s[1]) <=70)
    return isFirstGood and isSecondGood

print(checkOrd('0E'), checkOrd('G0'))
# %%
def isMAC48Address(inputString):
    try:
        all = inputString.split('-')
        if len(all) !=6:
            return False
        for s in all:
            if len(s) != 2:
                return False
            int(s,16)
        return True
    except:
        return False

#%%
'''
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
'''
# %%
inputStr = "aabbbc"
sList = []
i = 0
while i < len(inputStr):
    s = inputStr[i]
    j = i
    print(f"\ni is {i}, j is {j}")
    if j < len(inputStr) - 1:
        while inputStr[j] == inputStr[j+1]:
            s += inputStr[j+1]
            j += 1
            i = j
            if j == len(inputStr) - 1:
                break
            
            print(f"i is {i}, j is {j}, {s}")
        
    sList.append(s)
    print(sList)
    i += 1
    print(i)
    
# %%
for i, s in enumerate(sList):
    sLen = len(s)
    if sLen >=2:
        sList[i] = str(sLen)+s[0]
print(''.join(sList))
#%%
# inputStr = "aabbbc"
inputStr = 'abbcabb'
sList = []
i = 0
while i < len(inputStr):
    
    j = i
    i += 1
    s = inputStr[j]

    print(f"\ni is {i}, j is {j}, s is {s}")
    if j < len(inputStr) - 1:
        while inputStr[j] == inputStr[j+1]:
            s += inputStr[j+1]
            j += 1
            i = j
            print(f"i is {i}, j is {j}, s is {s}")
            if j == len(inputStr) - 1:
                break  
    # 
    sList.append(s)
    print(sList)
# %%
