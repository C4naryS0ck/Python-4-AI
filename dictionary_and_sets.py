"""info = {
    'key': 'value',
    'name': ['Arjun', 'Anshul', 'Aman'],
    'subjects': ('Math', 'Science', 'English'),
    'age': 20,
    'is_student': True,
    98.99 : 98
} 
print(type(info)) 
print(info['key']) 
print(info['name']) 
print(info['age']) 
info ['is_student'] = False
info['surname'] = 'Sharma'
print(info) 

empty_dict = {} 
empty_dict['name'] = 'CUJ'
print(empty_dict)  

#NESTED DICTIONARIES
student = {
    'name' : 'abhishree',
    'subjects' : {
        'maths' : 4,
        'dsa' : 4,
        'english' :3
    } 
}
print(student) #accessing the nested dictionary
print(student['subjects']) #accessing the inner dictionary
print('\n',student['subjects']['english']) #accessing the value of english in the inner dictionary
print(student.keys()) #returns the keys of the dictionary
print(list(student.keys())) #returns the keys of the dictionary in list. (type casting)
print('\n')
print(len(student)) #returns the number of key-value pairs in the dictionary
print('\n')
print(student.values()) #returns the values of the dictionary 
print(list(student.values())) #returns the values of the dictionary in list. (type casting)
print(student.items()) #returns the key-value pairs of the dictionary as a list of tuples.
print(list(student.items())) #returns the key-value pairs of the dictionary as a list of tuples. (type casting)'''

print(student['name2']) #error because the key 'name2' does not exist in the dictionary.
print(student.get('name2')) #returns None because the key 'name2' does not exist in the dictionary. 
student.update({'city': 'alahabad'}) #adds the key-value pair to the dictionary.
print(student) """ 

#SETS
abc = {1,2,3,4,5,5,5,5}
#print(abc) #sets do not allow duplicate values.
#print(type(abc)) 
#print(len(abc)) #returns the number of unique elements in the set. 

collection = set()
#print(type(collection)) 
collection.add(2)  #adds the value to the set.
print(collection)
collection.remove(2) #removes the value from the set.
print(collection) 
collection.add('abhishree')
#collection.add([1,2,3]) #error because lists are mutable and cannot be added to a set.
print(collection)
collection.clear()
print(collection) #returns an empty set.
collection.add(1)
collection.add('abhihs')
collection.add('hellp')
collection.add('coding') 
#print(collection.pop())
#print(collection.pop())
ab = {1,2,3,4,5}
cde = {3,7,8,9} 
union = ab.union(cde) #returns a new set that contains all the unique elements from both sets.
print(union) 
inter = ab.intersection(cde) #returns a new set that contains only the elements that are present in both sets.
print(inter)