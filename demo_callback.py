# %% 
'''
Callback: 
1. function a (main, minimize functions) calls function b (objective function, utility function, or something else), and wants to make b run a specific independent task at some point during b's execution. 
2. We want to be able to vary which chunk of code gets called in different calls to b, so it cannot be hard-coded inside b (for examples, hard to give b what specific inputs needed). 
3. Solution is to introduce c (callback), to b, as one argument, and b uses that parameter c to call the functionality that a wants b to call. 
4. Function b may pass some parameters to the function represented by c, when it calls it. These could be either internally generated, passed from a, or a combination of both. So, by changing the value of the function c that gets passed to b (on different calls to b), a can change what chunk of code b calls.
5. We can passed different callbacks to a, we could enhance a in a different way, without changing the code of the a function itself. This leads to code with less coupling, which is generally preferable for modularity and maintainability.
'''
# %%
def report_progress(i, result):
    print(f"\nItems added: {i}. Running result: {result}.\n")

def square(x):
    return x**2

def main(func, num_calls, report_interval, callback):
    '''
    a fancy way of computing sum of squares
    add i**2 from i =1 till i = num_calls
    '''
    print(f"Entered main(): total number of calls = {num_calls}, report_interval = {report_interval}, callback = {callback.__name__}\n\n")
    result = 0
    print("Processing ...\n")
    for i in range(1, num_calls + 1):
        # print(f'{i}-th call of the function {func.__name__}\n')
        result += func(i)
        if i % report_interval == 0:
            # This is the call to the callback function 
            # that was passed to this function.
            callback(i, result)
    return result
 
main(square, 12, 5, callback=report_progress) # no explicit input is given to report_progress

#%%
def func1(a,b):
    print(f"we are summing up {a} and {b}")
    # return a+b

def func2(a,b,func):
    func1(a,b)
    return a+b

func2(1,2,func1)
# %% f-string, or function string
from time import time
print("1+2")
print(f"{1+2}") # inside {} gets eval()
print(f"Right now is {time()} in seconds")
# %%
