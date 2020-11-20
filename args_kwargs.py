# def func1(a,b,c,d):
#     print(a,b,c,d)

# keep normal first then args then kwargs

def funargs(normal,*args, **kwargs):
    print(normal)
    for items in args:
        print(items)
    for key,value in kwargs.items():
        print(f" for {key} value is {value}")

har = ["moha","kumar","tanisha","negi","shivam"]

kw = {
    "name":"mohan",
    "class":"thenth",
    "school":"vishvas"
}
funargs("this is normal", *har, **kw)