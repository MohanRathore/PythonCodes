# __ se suru hone wale and __ se end hone wale methods hote hai dunder methods

class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalry,arole):
        self.name = aname
        self.salary = asalry
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name} salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

    def __add__(self, other):  # dunder method
        return self.salary + other.salary

    def __truediv__(self, other):
        return  self.salary/other.salary

    def __repr__(self):
        return self.printdetails()

harry = Employee("Harry",500,"programmer")
rohan = Employee("rohan",130,"cleaner")

print(harry+rohan)

print(harry)