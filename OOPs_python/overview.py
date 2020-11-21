# object oriented programming concepts
# Classed - Template
# object - for a particular class(Insantance of the class)
# OOps uses DRY -(dont repeat yourself)
# get_no_of_filmes(srk)

class Student:
    pass

harry = Student()  # instance of class
larry = Student()

print(harry)
print(larry)

harry.name = "harry"   # variable of instance
harry.std = 12
harry.section = "A"

print(harry.name)
print(harry.std)