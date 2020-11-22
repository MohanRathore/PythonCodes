# hamesha intance varibale ki priorty jayda hoti hai compared to class variable
class A:
    classvar1 = "I am class variable in  class A"
    def __init__(self):
        self.var1 = "I am inside class A constructor"
        self.classvar1 = "I am instance variable in Class A"
        self.special = "special"

class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B constructor"
        self.classvar1 = "I am instance variable in Class B"


a = A()
b= B()
print(b.special)
print(b.var1)
print(b.classvar1)