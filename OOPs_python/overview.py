# object oriented programming concepts
# Classed - Template
# object - for a particular class(Insantance of the class)
# OOps uses DRY -(dont repeat yourself)
# get_no_of_filmes(srk)

# class Student:
#     pass
#
# harry = Student()  # instance of class
# larry = Student()
#
# print(harry)
# print(larry)
#
# harry.name = "harry"   #  instance variabele of object
# harry.std = 12
# harry.section = "A"
#
# print(harry.name)
# print(harry.std)

class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
larry = Employee()

harry.name = "harry"
harry.salary = 800
harry.role = "Teacher"

larry.name = "larry"
larry.salary = 1000
larry.role = "police"

print(harry.no_of_leaves)
harry.no_of_leaves = 10
print(Employee.no_of_leaves)
print(harry.salary)
print(harry.__dict__)  # dict of an object 