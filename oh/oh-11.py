#%%
import numpy as np
# %%
'''
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc.
'''

for i in range(97,97+26):
    print(chr(i))
# %%
# inputString = "bbbaacdafe"
inputString = "aabbb"
def isBeautifulString(inputString):
    alphabet = [chr(i) for i in range(97, 123)]
    count = inputString.count(alphabet[0])
    for s in alphabet[1:]:
        count_new = inputString.count(s)
        if count_new > count:
            return False
        count = count_new
    return True
print(isBeautifulString(inputString))
    

# %%
import string
r = [inputString.count(i) for i in string.ascii_lowercase]

r[::-1] == sorted(r)
# %%
'''
An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.

Given a valid email address, find its domain part.
'''

address = "\"very.unusual.@.unusual.com\"@usual.com"
print(address)
print(address.rfind('@'))
print(address.split('@')[-1])
# %%
'''
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.
'''
st = "abcdc"
def buildPalindrome(st):
    n = len(st)
    for i in range(n):
        st_new = st + st[:i][::-1]
        print(n, st[:i][::-1], st_new)
        if st_new[::-1] == st_new: 
            return st_new
print(buildPalindrome(st))



# %%
