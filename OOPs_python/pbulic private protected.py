# public -
# protected -
# private -

class Employee:
    no_of_leaves = 8
    _protec = 110
    __private = "private"
    def __init__(self,aname,asalry,arole):
        self.name = aname
        self.salary = asalry
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name} salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

    #class method as a altenative constructor
    @classmethod
    def from_str(cls,string):
        # param = string.split("-")
        # return cls(param[0],param[1],param[2])
        # one liner
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("This is good " + string)

harry = Employee("Harry",800,"Teacher")

print(harry._protec)
print(harry._Employee__private)