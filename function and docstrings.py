# built in function
a = 5
b = 6
c = sum((a,b))
print(c)

# user defined functions
def func(a,b):
    print("You are in function",a+b)

def func1(a,b):
    """ This is function to calculate average of two number"""
    avg =(a/b)/2
    return avg
v = func1(5,7)
print(v)
print(func1.__doc__)