# recursion is a function where a function call itself repeatedly.
# it is loops ka khatarnak version in a way. 

# create a function which first prints 5 then 4 then 3 then 2 then 1. 
def show(n):
    if n == 0:
        return
    print(n, end = " ")
    show(n-1) 


show(5) # 5,4,3,2,1 