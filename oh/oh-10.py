#%% solving python
import numpy as np
# %%
'''
Longest digit prefix
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
longestDigitsPrefix(inputString) = "123".
'''
inputString = "12abc34"
numString = ""
i = 0
while inputString[i].isdigit():
    print(inputString[i].isdigit())
    numString += inputString[i]
    # numString = numString.join([inputString[i]])
    i += 1
    print(numString)

def longestDigitsPrefix(inputString):
    i = 0
    numString = ''
    
    while inputString[i].isdigit():
        numString += inputString[i]
        i += 1 
        if i==len(inputString): break
    return numString

def longestDigitsPrefix1(inputString):
    return re.findall('^\d*',inputString)[0]
# %% digit degree
'''
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.
'''
n = 91
degree = 0
while n >= 10:
    digits = str(n)
    n = sum([int(s) for s in digits])
    degree += 1

def digitDegree(n):
    if n < 10:
        return 0
    sumOfDigits = sum([int(i) for i in str(n)])
    return digitDegree(sumOfDigits) + 1
    
# %% bishop vs pawn
'''
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.
'''
bishop =  "a1"
pawn=  "c3"

def bishopAndPawn(bishop, pawn):
    return abs(ord(bishop[0])-ord(pawn[0]))==abs(int(pawn[1])-int(bishop[1]))

# %%
