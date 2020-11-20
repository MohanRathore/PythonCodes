# lambda function or anonymous function
def add(a,b):
    return a+b

minus = lambda x, y: x+y

print(add(2,4))
print(minus(3,8))


list = [[11,41],[5,6],[8,23]]

list.sort(key=lambda x:x[0])
print(list)