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

harry = Employee("Harry",800,"Teacher")
larry = Employee("Mohan",10000,"Programmer")
mohan = Employee.from_str("minku-5000-student")

print(mohan.no_of_leaves)