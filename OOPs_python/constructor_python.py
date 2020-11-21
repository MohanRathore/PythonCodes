class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalry,arole):
        self.name = aname
        self.salary = asalry
        self.role = arole
    def printdetails(self):
        return f"Name is {self.name} salary is {self.salary} and role is {self.role}"
    pass

harry = Employee("Harry",800,"Teacher")
larry = Employee("Mohan",10000,"Programmer")

# harry.name = "harry"
# harry.salary = 800
# harry.role = "Teacher"
#
# larry.name = "larry"
# larry.salary = 1000
# larry.role = "police"
# larry.no_of_leaves = 10

print(harry.printdetails())
print(larry.printdetails())
print(larry.no_of_leaves)