# File IO basics
"""
"r" - open file for read mode  default mode
"w" - open file in write mode
"X" - if file does not exist than create one
"a" - add more content to file
"t" - text mode  default mode
"b" - binary mode
"+" - read and write
"""
# reading a file
# f = open("Harry.txt","rt")
# content = f.read()  #print number of charcter in functions
# content = f.read(344)  #print number of charcter in functions
"""    
for line in f:     #print line by line
    print(line, end="")
"""
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# f.close()

# writing and appending into files
# f = open("Harry.txt","a")
# a = f.write("Harry is good guy\n")
# print(a)
# f.close()
f = open("Harry.txt","r+")  # handel read and write both modes
print(f.read())
a = f.write("Harry is good guy\n")
print(a)
f.close()