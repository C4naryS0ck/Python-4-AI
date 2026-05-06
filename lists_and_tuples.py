'''marks = [33,45,6,7,8,8,5,4,3,2,2]
print(marks)
print(type(marks))
print(marks[3])
print(len(marks))
#mutation
marks[0] = 'arjun'
print(marks) 
print(marks[0:5]) # slicing 

print(marks.append(100)) #adds that value to the end.
print(marks)'''
'''
list = [12.4,56,7,85,3,3,23,2,23,4,5,5,545]
print(list.sort()) #sorts the list in ascending order - same data type.
print(list) 
print(list.sort(reverse=True)) #sorts the list in descending order. 
print(list) 
list1 = [3,1,2]
print(list1.reverse())
print(list1)
print(list1.insert(1,43)) 
print(list1) 
list1.remove(1) #removes the first occurrence of the value.
print(list1) 
list1.pop(2) #removes the value at the index and returns it.
print(list1)  
print(list)'''

'''tup = (12,3,4,3,3,3,5,'hello')
print(tup)
print(type(tup))
print(tup.index(12)) #returns the index of the first occurrence of the value.
print(tup.count(3)) #returns the number of times the value occurs in the tuple. 
''' 
#ques : 
'''movies = list(input('enter the names of top 3 movies: ').split(','))  
print(movies) 
print(type(movies))
'''

"""
# wap to check if the list is palindrome or not.
elements = list(input('enter any number elements: ').split(',')) 
list = elements.copy()
print(elements) 
print(list) 
x = []
list.reverse()
print(list) 

if list == elements:
    print('palindrome') 
else:
    print('not palindrome')""" 

'''tup = ("C","D","A","A","B","B","A")
print(tup.count("A")) 

list = list(tup)
list.sort()
print(list)'''