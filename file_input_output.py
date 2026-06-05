"""
r = reading mode
w = writing mode
x = creating mode and open it for reading
a = open for writing, appending to the end of the file if it exists
t = text mode(default)
b = binary mode
+ = open a file for updating (reading and writing)
"""
"""
# reading from a file.
f = open("demo.txt","r") #opens the file in read mode) 
data = f.read() #reads the entire file and stores it in a variable data.
print(data)
print(f.readline())
print(f.readline())
print(f.readline())
f.close()  
"""
"""
#writing to a file: 2 options - w or a. w will overwrite the existing data 
# and a will append to the end of the file.

f = open("demo.txt","a") #opens the file in write mode. 

f.write("\nthis is learning to append at the end in the existing file.") #writes the string to the file.

f.close() 
"""

f = open("sample.txt","a")

f.close()