# single Inheritance
class Employee:
    no_of_leaves = 8
    var = 8
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

class Player:
    no_of_games : 4
    var = 9
    def __init__(self,aname, agame):
        self.name = aname
        self.game = agame

    def printdetails(self):
        return f"Name is {self.name} gmae is {self.game} "

class CoolProgrammer(Employee,Player):  # jo phei class hai uska constructor call krega
    language = "c++"
    var = 10
    def printlanguage(self):
        print (self.language)

harry = Employee("Harry",800,"Teacher")
rohan = Employee("rohan",10000,"Programmer")
shubham = Player("shubham",["cricket","football"])
mohan = CoolProgrammer("mohan",500000,"coolprog")

print(mohan.var)