# list = სია

# ordered, allows duplicates, changeable.

from cgi import print_arguments


mylist = ["george", 1, 2, "andria", True, False, 5.5]

print(mylist)

 # რაიმეს დამატება ლისტის ბოლო ადგილას
# mylist.append("math_program")

# print(mylist)

 # ლისტს ვაკლებთ მე 4 ინდექსზე მდებარე სახელს
# mylist.pop(4)

# ლისტიდან ვშლთ რაიმე მონაცემს
# mylist.remove(1)

# ლისტს არ გააჩნია ADD ფუნქცია
# print(mylist)

print(len(mylist))

n = len(mylist)

print(mylist[len(mylist) - 2])

print(mylist[-1])

print(mylist[n - len(mylist)])

mylist[3] = "george is pro"

print(mylist)


mylist[1] = "itachi is best"
mylist[2] = "madara is strongest uchiha"
mylist[4] = " naruto is stronger then saitama"
mylist[5] = " naruto shipuden is best anime"
mylist[6] = " naruto shipuden  is better then dragon ball z"
mylist[0] = "sakura is trash"
print(mylist)


# set = სიმრავლე
# unordered
# inchangeable
# does not allow duplicates

myset = {1, 2, 3, 4, 5, "george"}

print(myset)

myset.add("george or andria:")
print(myset)
myset.remove(1)
print(myset)
myset.remove(5)
myset.remove(2)
myset.remove(3)
myset.remove(4)

print(myset)

myset.add("george")

print(myset)

words = {"hello", 1, 3.14, 1}
new_set = words.union(myset)
print(new_set)

cars = {"ბეემვე", "ლამბორჯინი", "ბუგატი"}

new_set.update(cars)
print(new_set)

 

        
# tuple = ტუპლი