from turtle import *

# tuple = ტუპლი
# unchangeable, orderded, allows duplicates nad different data types

mytuple = (1, 2, "python", True)

# რამდენ ელემენტს შეიცავს ტუპლი
print(len(mytuple))

print(mytuple)

print(mytuple[2])

mylist = list(mytuple)

mylist.append("coffe bar")
mylist.remove(True)
mylist[3] = "Naruto"
mylist.index("Naruto")
print(mylist)

print(len(mylist))
print(mylist[len(mylist)-1])

mytuple = tuple(mylist)
print(type(mytuple))
print(type(mylist))




# dictionary = ლექსიკონი

car = {"brand": "toyota"
        }