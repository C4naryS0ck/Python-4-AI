"""i = 1 
while i<=2:
    print('hello')
    i += 1 

#print numbers from 1 to 100 and in reverse order from 100 to 1.
i = 1
while i<=100:
    print(i)
    i += 1 
print("loop ended") 

i = 100
while i >=1:
    print(i)
    i -=1
print('reverse loop ended')  
"""
"""# print multiplication table of a number entered by user.
num = int(input('enter a number: '))
i = 1
while i <= 10:
    print(num*i)
    i += 1 
""" 
"""# ques: print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
i = 1
j = 1
while i<=100: 
    while j <= 19:
        print(i)
        j += 2
        i += j

# ques: print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
i = 1 
while i<= 10:
    print(i*i)
    i += 1 
"""
"""
#Search for a number x in this tuple using loop:
tup = (1,4,9,16,25,36,49,64,81,100 )
num = int(input("enter a number : ")) 
left = 0
right = len(tup) - 1 
found = False
while left<=right:
    mid = (left+right)//2 
    if tup[mid] == num:
        print("number found at index:",mid) 
        found = True

    if num<tup[mid]:
        right = mid - 1
    else:
        left = mid + 1 
if not found: 
    print('Number not found.') 
"""
"""#Search for a number x in this tuple using loop:
tup = (1,4,9,16,25,36,49,64,81,100 )
i = 0
num = int(input('enter a number:'))
while i<len(tup):
    if tup[i]==num:
        print("found at index:",i)
        break
    i += 1 
"""
"""# working of continue keyword.
i = 0
while i<=5:
    if (i==3):
        i += 1
        continue #acts as skip.
    print(i) 
    i += 1 
"""
#  FOR LOOPS:
"""num = [1,2,3,4,5]
veggies = ['potato','brinjal','ladyfinger','cucumber']
for val in veggies:
    print(val)

tup = (1,2,3,4)
for num in tup:
    print(num)"""

"""str = 'abhishree'
for ch in str:
    print(ch)
else:
    print('end')

"""
"""list = [ 1,4,9,25,36,49,64,81,100]
for el in list:
    print(el)

i = 1
for el in range(10):
    print(i*i)
    i+=1
""" 
"""
tup = (1,4,9,25,36,49,64,81,100)
num = int(input("enter a number:")) 
idx = 0 #variable used to keep track of index
for i in tup:
    if (num == i):
        print("found at index:",idx ) 
    idx +=1 
    """

"""
# printing the multiplication of a number.
n = int(input("enter a number: "))
for i in range(1,11):
    print(n*i)

for i in range(5):
    pass 
print("understanding the use of function pass!") """

"""
# ques: WAP to find the sum of first n numbers. using while.
num = int(input("enter the numbers upto which you want the sum.: "))
sum = 0
while num != 0:
    print(num)
    sum = sum + num
    num -=1
print("sum of first n numbers is:", sum) 
# SOLVED USING FOR LOOP: 
for i in range(1,num+1):
    sum = sum +i
print("sum of first n numbers is:",sum) 
"""

"""
# WAP to find the factorial of first n numbers. using for
n = int(input('enter the number to find the factorial of: '))
fact = 1
for i in range(1,n+1):
    fact = i * fact 
    i += 1
print("factorial is: ",fact) 

# SOLVING USING WHILE: 
while n != 0:
    fact = fact * n
    n -= 1
print(fact)
"""