"""
print(1+2) #3
print("apna"+"college") # concatenate
print([1,2,3,4]+[5,6,7,8]) # merge 
# (above) this is polymorphism - same "+" operator behaving in 
# different manner. 

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i+",self.img,"j") 

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)
    

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,3)
num2.showNumber()
# how to add these two number? 1i+3j and 4i+3j. as + is not defined for complex numbers
# we use DUNDER FUNCTIONS. 

num3 = num1 + num2
num3.showNumber() 

num4 = num1 - num2
num4.showNumber()
"""

# ITS TIME FOR PRACTICE QUESTIONSSSS!!!!
"""
# QUES: Define a Circle class to create a circle with radius r using 
# the constructor. Define the area() method of the class which calculates 
# the area of the circle. Define a perimeeter() mehtod of 
# the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        print((22/7)*self.radius **2)
    
    def perimeter(self):
        print(2 * (22/7) * self.radius)

c1 = Circle(21)
c1.area()
c1.perimeter()
"""
"""
# ques: define a Employee class with attributes role, department, 
# salary. This class should also have showdetials() method. Create an 
# Engineer clss that inherits properties from Employee and has the 
# attributes : name & age.

class Employee:
    def __init__(self, role, department, salary): 
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print("role = ", self.role)
        print("department = ", self.department)
        print("salary = ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer","it","75,000") 

engg1 = Engineer("Elon Musk",40)
engg1.showDetails()
"""

# QUES: create a class called Order which stores item and its price. 
# Use dunder function __gt__() to convey that: order1 > order2 if 
# price of order1 > price of order2


class Order:
    def __init__(self, item, price):
        self.item = item 
        self.price = price 
    
    def __gt__(self, odr2):
        return self.price > odr2.price
o1 = Order("Chips",20)
o2 = Order("tea",15)
print(o1>o2)
