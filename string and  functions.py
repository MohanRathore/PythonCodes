mystr = "harry is a good boy"
print(mystr)
print(mystr[4])
print(mystr[0:5])
print(mystr[0:19])
print(mystr[0:99])  #not give any error just print the rest string
print(len(mystr))

#if you want to skip one character
print(mystr[0:5:2])
print(mystr[0::2])
print(mystr[::])
print(mystr[::-1])
print(mystr[::-2])


# STRING FUNCTIONS
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","are"))