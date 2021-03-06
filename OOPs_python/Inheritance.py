# single Inheritance
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


class Programmer(Employee):  #single inhertance inherited Emplyee class
    def __init__(self,languages):
        super()
        self.languages = languages

    def printprog(self):
        return f"Programmer Name is {self.name} salary is {self.salary} and role is {self.role} language is"



harry = Employee("Harry",800,"Teacher")
rohan = Employee("rohan",10000,"Programmer")

shubham = Programmer("shubham",500000,"coder","python")
karan = Programmer("karan",500,"coder")

print(karan.printprog())
print(karan.printdetails())
