'''
print("Hello, World!")
print("I am learning AI!!")
import requests 
response = requests.get("https://api.github.com")
print(response.status_code) #should return 200 if successful.

first_name = 'abhi'
last_name = "raj"

full_name = first_name+ last_name
print(full_name)

long_dash = "-" *10
print(long_dash)
print(len(long_dash))
print(len(full_name))

is_raining = True
print(is_raining) 
age = 16
can_vote = age >=18
print(can_vote) 

age = 25
has_license = True
drunk = False
can_drive = age >= 16 and has_license and drunk !=True
print(can_drive)



string = "hi my name is if"
name = f'if {string}'
print(name)  
'''

"""name = "abhishree" # string variable
age = 33
price = 23.444"""

"""print("my name is:",name)
print("my age is:",age)
print("my price is:",price) 
print(type(name))
print(type(age))    
z = None
print(type(z))
print(z)
"""
#print sum
"""a = 2
b = 3
sum = a+b
print(sum) 
print(a+b)
print(a-b)"""
#arithem operators
z = 5
x = 2
"""print(z+x)
print(z-x)
print(z*x)
print(z/x)
print(z//x) #floor division
print(z%x) #modulus
print(z**x) #exponentiation
print(z==x)
print(z!=x)
print(z>x)
print(z<x)
print(z>=x)
print(z<=x)"""

#logical operators
'''a = 50
b = 30
print(not False)
print(not True) 
print(a>b and b<a)
print(a>b or b<a) 
print(not(a>b and b<a))
print(not(a>b or b<a)) '''

'''#type conversion
a,b  = 1,2.0
print(int(a+b))

h = 3.13
h = str(h)
j = 'u'
print(type(h),h+j)'''
'''
#input function
name = input("what is your name? ")
print("welcome",name) 

name1 = int(input("what is your name? "))
print("welcome",name1) ''' 

'''#Ques: WAP to input 2 numbers & print their sum.
a = int(input('enter a number:'))
b = int(input('enter 2nd number:'))
print("sum is:",a+b)

#ques: wap to input side of a square & print its area.
s = int(input("enter the side of square:"))
print("area of sqauare is:",s*s)'''

#ques: wap to input 2 floating point numbers and print their average.
f1 = float(input("enter 1st number: "))
f2 = float(input("enter 2nd number: "))
print("average is:",(f1+f2)/2)

#ques: wap to input 2 int numbers, a and b. Print true if a is greater
#than or equal to b. If not print False.
a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))   
print(a>=b)