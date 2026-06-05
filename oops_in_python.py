"""
# creating class
class Student:
    name = "abhishree"
# creating object of class
s1 = Student()
print(s1.name)  # Output: abhishree
"""
"""
# Understand the concept of constructors. 
class Car:
    color = "red"
    brand = "BMW"
    def __init__(self,name,price):
        self.name = name # name is a new variable which has value fullname.
        self.price = price
        print("adding new student in database")
        
car1 = Car('karan', 10000)
print(car1.name,car1.price) # Output: karan
car2 = Car('rohan', 15000)
print(car2.name,car1.price) # Output: rohan 
"""
"""
class Marks:
    # default constructor
    def __init__(self):
        print("this is default constructor")

    # parameterized constructor
    def __init__(self,marks):
        self.marks = marks
        print("this is parameterized constructor")
    
m1 = Marks(122)
print(m1.marks) 
"""
"""
# CLASS AND INSTANCE ATTRIBUTES
class Student:
    # class attribute
    # stored once in the memory and shared by all instances of the class
    school = "ABC School" 
    
    def __init__(self, name, age):
        # instance attributes
        # they get stored countless times in the memory for each instance of the class
        # as they are unique to each instance of the class.  
        self.name = name
        self.age = age 
    
s1 = Student("Alice", 20)
s2 = Student("Bob", 22)
print(s1.name)  # Output: Alice
print(s2.name)  # Output: Bob
print(s1.school)  # Output: ABC School
print(s2.school)  # Output: ABC School
"""
"""
# METHODS IN OOPS 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome to the class!",self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Alice", 20)
s1.welcome()  # Output: Welcome to the class! 
print(s1.get_marks())  # Output: 20
"""
"""
# QUESTION : create a student class that takes name and marks of 3 subjects 
# as arguments in constructor. Then create a method to print the average.
# SOLUTION : 
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def average_marks(self):
        total = sum(self.marks)
        average = total / len(self.marks)
        return average
    
s1 = Student("alice", [85, 90, 78])
print(s1.average_marks())  # Output: 84.33333333333333
"""
"""
# STATIC METHODS IN OOPS
class Student: 
    @staticmethod  # this is a decorator which is used to define a static method in a class.
    def welcome():
        print("Welcome to the class!") 
Student.welcome()  # Output: Welcome to the class!
"""
"""
# ABSTRACTION AND ENCAPSULATION IN OOPS
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True 
        print("car started...") 
    
car1 = Car()
car1.start()  # Output: car started
# here we are hiding the internal details of how the car is started and 
# providing a simple interface to the user to start the car. This is abstraction.

# abhi tak jo bhi kiya hai that is all encapsulation. 
# We have encapsulated the data and the methods that operate on the 
# data within a single unit called class.
"""

# building a mini banking system using OOPS in python.
# QUES: create account calss with 2 attributes - balance and account no.
# Create methods for debit, credit and printing the balance.
class Account:
    def __init__(self, balance, acc): 
        self.balance = balance 
        self.account_number = acc

        # DEBIT METHOD
    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Debited {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance") 
        
        # CREDIT METHOD
    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance: {self.balance}")
    
        # GET BALANCE METHOD
    def get_balance(self):
        return self.balance
        
acc1 = Account(10000, 123456789)
acc1.debit(200)  # Output: Debited 200. New balance:
acc1.credit(500)  # Output: Credited 500. New balance: 1300
print(acc1.get_balance())  # Output: 1300