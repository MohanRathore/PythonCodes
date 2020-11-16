# LIST IN PYTHONS MUTABLE
grocery = ["harpic","mohan","kumar","rathore","tanisha","surabhi",6862,34.56]
print(grocery[1:])

numbers = [27,45,76,23,88,99]
#numbers.sort()
#numbers.reverse()
numbers.append(71)
numbers.insert(1,71)
numbers.remove(99)
numbers.pop()
print(numbers)

# TUPLES IN PYHTONS   IMMUTABLE LIST IS CALLED TUPLES

# for tuple with single value we have to put one comma extre with it
tp1 = (1,)
print(tp1)
tp =(1,2,3)
print(tp)


a=4
b=6
a ,b = b ,a
print(a)
print(b)

# DICTIONARY IN PYTHON
dict = {
    "Harry":"Burger",
    "Rohan":"fish",
    "Skillf":"pratha",
    "Shubham": {"breakfast":"maggie", "lunch":"roti", "dinner":"chicken"}}
print(dict["Rohan"])
print(dict["Shubham"]["breakfast"])
dict["Ankit"] = "fast food"
dict[420] = "kabbas"
print(dict)
del dict[420]
print(dict)

# never do d3 dict
d3 = dict.copy()
print(dict.get("Harry"))
dict.update({"Leena":"Toffes"})
print(dict.keys())
print(dict.items())
# In dict key should be immutable

# SETS IN PYTHON

s = set()

s_from_list = set([1,2,3,4,5])
print(s_from_list)
print(type(s_from_list))

s.add(3)
s.add(3)
s.add(2)
s.remove(3)
s = s.union({2,3,4,5})
s = s.intersection({4,8,4,5})
print(s)