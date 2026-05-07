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
