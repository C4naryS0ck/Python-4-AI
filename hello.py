print("Hello, World!")
print("I am learning AI!!")
'''import requests 
response = requests.get("https://api.github.com")
print(response.status_code) #should return 200 if successful.
'''
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