# recursion is a function where a function call itself repeatedly.
# it is loops ka khatarnak version in a way. 
"""
# create a function which first prints 5 then 4 then 3 then 2 then 1. 
def show(n):
    if n == 0: # this is the base case so that the program doesn't crash.
        return
    print(n, end = " ")
    show(n-1) 
show(5) # 5,4,3,2,1 

def factorial(n):
    if (n == 0 or n==1):
        return 1
    else:
        return (n*factorial(n-1))

print(factorial(5))
"""
"""
# write a recursive function to calculate the sum of first n natural numbers. 
def natural_sum(n):
    if n == 1:
        return 1
    else: 
        return (n + natural_sum(n-1))
print(natural_sum(3)) 
"""
"""
# write a recursive function to print all elements in a list. 
# HINT : use list and index as parameters.
def elements(l):
    for i in l:
        print(i) 
list = [1,2,3,4]
elements(list)
"""

def el(l,idx = 0):
    if idx == len(l):
        return 
    print(l[idx], end = " ")
    el(l,idx+1)

list = [5,6,7,8] 
el(list)
