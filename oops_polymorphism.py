
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

