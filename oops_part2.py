"""
# DEL KEYWORD
class Student:
    def __init__(self,name):
        self.name = name 

s1 = Student("John")
print(s1.name)
del s1
print(s1) 
"""

# PRIVATE ATTRIBUTES AND METHODS: 
"""
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345","abcde")
print(acc1.acc_no) 
acc1.reset_pass() 
"""
"""
class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome()) 
# this throws error as it is private so it cannot be accessed from 
# outside the class.
"""

# INHERITANCE
"""
class Car:
    color = "white"
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stopped..") 

class ToyotaCar(Car):  
    def __init__(self,brand):
        self.brand = brand
# up until here this is an 
# example of single inheritance, as ToyotaCar is inheriting from Car class

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type
# The fortuner class is inheriting from ToyotaCar class, which is 
# inheriting from Car class, so this is an example of multilevel inheritance.   

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Innova")
print(car1.brand)
print(car1.start()) 
print(car1.color)
car3 = Fortuner("Diesel")
car3.start() 
"""
"""
# MULTIPLE INHERITANCE
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
"""
"""
class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..") 

class ToyotaCar(Car):  
    def __init__(self,name,type):
        self.name = name 
# here we are creating a different attribut in the child class. 
# but we want to use the type attribute of the parent class. 
# therefore we use the super() function to call the __init__ method of the parent class.
        super().__init__(type)
        super().start()
car1 = ToyotaCar("prius","electric")
print(car1.type) 
"""
"""
# CLASS METHOD 
class Person:
    name = "anonymous"
    
    def changeName(self,name):
        self.name = name

p1 = Person()
p1.changeName("rahul")
print(p1.name)
print(Person.name) # prints anonymous this means that class attribute is not changed 
# but instead the object name was changed. 

class Person:
    name = "anonymous"
    
    def changeName(self,name):
        #Person.name = name
        self.__class__.name = "rahul"

p1 = Person()
p1.changeName("rahul")
print(p1.name)
print(Person.name)

class Person:
    name = "anonymous"
    
    @classmethod
    def changeName(cls,name):
        cls.name = name
    # cls is referecing to the class and not self. 

p1 = Person()
p1.changeName("rahul")
print(p1.name)
print(Person.name) 
"""

# PROPERTY DECORATOR
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.math = math
        self.chem = chem
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Student(98.90,87,99)
print(stu1.percentage)

# now the teacher realised that the marks oh physics of student1 is 89.90. 
# this is what the teacher does:

stu1.phy = 7.90
print(stu1.phy)
print(stu1.percentage) # percentage did not change. But we need it to change right?
# we create a method def calcPercentage. 
# Now this is what it looks like..
stu1.phy = 7.90
print(stu1.phy)
stu1.calcPercentage()
print(stu1.percentage)

# another better way to do this is PROPERTY DECORATORS 
print("\nanother better method is PROPERTY DECORATORS\n")
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.math = math
        self.chem = chem
        
    #def calcPercentage(self):
    #    self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Student(98.90,87,99)
print(stu1.percentage)
stu1.phy = 90
print(stu1.percentage)