# f string   - inserting variables in string

me ="mohan"
a1 = 3
a ="this is %s %s"%(me,a1)

aa = "This is {} {}"
b = aa.format(me ,a1 )
print(b)

aaa = f"this is {me} {b} {a1} {4+5}"
print(aaa)