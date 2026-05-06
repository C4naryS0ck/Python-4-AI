"""str = 'this is apna college\'s tutorial'
print(str)

str1 = '''this is a string
we are creating it in python''' 
print(str1

#concatination
print( len(str + "\n" + str1))

#INDEXING
print(str[3::2]) 
print(str.endswith('al'))
print(str.endswith('er'))
abhishree = 'abhishree shree jii'
capt = abhishree.capitalize()
print(capt) 
print(abhishree.replace('shree','shreemati')) 

print(abhishree.find('q')) 
print(abhishree.count('shree')) 
"""
'''#ques: wap to input user's first name and print its length. 
name = input("enter first name: ")
print(len(name))

#
str = input("enter a string of your choice: ")
print(str.count('$')) ''' 

"""age = int(input("enter your age: "))
if(age >= 18):
    print("can vote")
    print("can drive")
else:
    print('cannot!') 

light = 'red'
if (light =='red'):
    print("stop")
elif (light == 'yellow'):
    print("look")
else:
    print("go")

print("end of code") 
"""
"""num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

if (num1 >num2) and (num1 >num3):
    print(f"{num1} is the greatest number")
if (num2 > num1) and (num2 > num3):
    print(f"{num2} is the greatest number")
if (num3 > num1) and (num3 > num2):
    print(f"{num3} is the greatest number")
else:
    print("all numbers are equal")

num = int(input("enter a number: "))
if num%7 == 0:
    print(f"{num} is divisible by 7")
else:    
    print(f"{num} is not divisible by 7")"""

a = int(input("enter a 1 number: "))
b = int(input("enter a 2 number: "))
c = int(input("enter a 3 number: "))
d = int(input("enter a 4 number: ")) 
if (a>b) & (a>c) & (a>d):
    print(f"{a} is the greatest number")
elif (b>c) & (b>d):
    print(f"{b} is the greatest number")
elif (c>d):
    print(f"{c} is the greatest number")
else:
    print(f"{d} is the greatest number")
    