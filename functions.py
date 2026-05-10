"""def calcSum(a,b): # a,b is parameters
    return (a + b) 
print(calcSum(2,3))
"""
"""# function that print hello
def print_hello():
    print('hello')
print(print_hello())
"""
"""# function that prints the average of 3 numbers.
def avg3(a,b,c):
    print((a+b+c)//3)
avg3(23,34,56) 
# DEFAULT ARGUMENTS
def calc_product(a =1,b=1):
    print(a*b)
    return a*b
calc_product(2,2) 
"""
"""# ques: WAP to print the length of a list. (list is a parameter) 
def list_len(list):
    print(len(list))

list = [1,2,3,4,5,6]
list_len(list)"""

"""# ques: write a function (WAF) to print the elements of a 
# list in a single line.(list is a paramter) 
def print_el(list):
    for el in list:
        print(el,end= " ")    
a = [1,2,3,4]
b = ["abhishree","raj","vamshi"] 
print_el(a)
print_el(b)
"""
"""# ques: WAF to find the factorial of n. (n is the parameter)
def factorial(n):
    fact = 1
    for i in range(1,n+1): 
        fact = fact * i
        n += 1
    print(fact)
factorial(6)
"""
"""
# ques : WAF to convert USD to INR. 
def conversion(usd):
    print(usd*94) 
conversion(1)"""

"""# ques: num ko input, function - if odd print string odd, if even print string even. 
def even_odd(a): 
    labels = ["Even","Odd"]
    print(labels[a % 2])
even_odd(5)""" 