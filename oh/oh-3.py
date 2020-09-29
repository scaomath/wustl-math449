#%% commonCharacterCount
import numpy as np
# %%
a = [1, 2, 5, 6]
b = [1, 2, 7, 8]
print(set(a+b))
# %%
s1 = "aabcc"
s2 = "adcaa"
s1_lst = [s for s in s1]
s2_lst = [s for s in s2]

set(s1_lst).intersection(s2_lst)
commonChar = set(s1_lst).intersection(set(s2_lst))
numCommonChar = 0
for s in commonChar:
    s1_count = [1 for i in s1_lst if i==s]
    s2_count = [1 for i in s2_lst if i==s]
    numCommonChar += min(len(s1_count), len(s2_count))
    
# %%
for s in commonChar:
    print(s)
# %% isLucky
n = 134008
digits = []
for i in [100000, 10000, 1000, 100, 10]:
    digits += [n // i]
    n -= i*(n // i)
    print(n)
digits += [n]
print(sum(digits[:len(digits)//2]))
print(sum(digits[len(digits)//2:]))
# %%
n = 1340
digits = []
for s in range(6):
    digits += [n % 10]
    if n // 10 >0:
        n = n // 10
    else:
        break
# %%
s = str(n)
pivot = len(s)//2
left, right = s[:pivot], s[pivot:]
sum(map(int, left)) == sum(map(int, right))

for i in map(int, right):
    print(i)

# %%
