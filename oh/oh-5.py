#%%
def areSimilar(a, b):
    diff = [a[i] != b[i] for i in range(len(a))]
    if sum(diff) > 2: 
        return False
    else:
        return set(a) == set(b)
# %%
a = [1,1,3,2]
b = [3,1,2,2]
areSimilar(a, b)
# %%
for i, j in zip(a,b):
    print(i,j)
# %%
sum(a != b for a, b in zip(a, b))
# %%
from collections import Counter as C
C(a)
# %%
inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbccccaaaaaaaaaaaaa"
count = {}
for s_ in inputString:
    count[s_] = sum([s==s_ for s in inputString])
sum([i%2 for i in count.values()])

# %%
