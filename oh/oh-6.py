#%%
import numpy as np
# %% check if a string is a valid ipV4 address
# x = ".316.254.1"
x = "01.233.161.131"
x = "172.16.254.1"
x = "0..1.0.0"
digits = []
while len(x) > 0:
    partition = x.partition('.')
    s = partition[0]
    if len(s) > 0 and s.isdigit():
        if len(s) == 1:
            digits.append(int(s)) 
        elif len(s) >= 2 and s[0] is not '0':
            digits.append(int(s))
    x = partition[-1]
print(digits)
# %%
def isIPv4Address(s):
    p = s.split('.')

    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)
# %% avoid Obstacles
# inputArray = [1, 4, 10, 6, 2]
inputArray = [2,3]
counter = 0
for i in range(1,max(inputArray)+1):
    isMultiple = [bool(k % i) for k in inputArray]
    if all(isMultiple): 
        break
print(i)
# %%
c = 2
while True:
    if sorted([i%c for i in inputArray])[0]>0:
        print(c)
        break
    c += 1
# %% blur a matrix of fixed size
def boxBlur(image):
    import numpy as np
    image = np.array(image)
    # filt = np.array([[1, 1, 1], 
    #                    [1, 1, 1], 
    #                    [1, 1, 1]])
    blur = np.zeros_like(image[1:-1, 1:-1])
    for i in range(1, image.shape[0]-1):
        for j in range(1, image.shape[1]-1):
            blur[i-1, j-1] = np.mean(image[i-1:i+2, j-1:j+2])
    return blur.tolist()