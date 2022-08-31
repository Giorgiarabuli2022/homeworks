# list = სია

# allows different data tipes - შესაძლებელია სხვადასხვა ტიპის მონაცემების ერთ ლისტში შენახვა
# changeable - ცვალებადი
# len() - length: ზომა/სიგრძე
# სხვადასხვა გვარად წარმოდგენა ერთი და იგივე მონაცემის
# changeable
# .append() - ამატებს ახალ ელემენტს mylist ის ბოლო ინდექსზა
# .pop() - აკლებს ელემენტს ბოლო ინდექსზე
# set - სიმრავლე


mylist = [1, 2, "dato", "ana", True, False, 3.0, "დათო", "საქართველო"]

print(len(mylist))

mylist.append("თბილისი - georgi, george is pro")
 
print(mylist)

print(len(mylist))

mylist.pop(6)

print(len(mylist))
print(mylist)

mylist.remove("ana")


# set - სიმრავლე


# დაულაგებელი
myset = {1, 2, "ana", "saqartvelo", 1 }

print(myset)

print(myset)

print(len(myset))

myset.pop()

print(myset)

myset.remove("ana")

print(myset) 



names = ["Giorgi", "Elene", "Dato", "Giorgi"]
names_set = set(names)
print(names_set)


myset = {"ana", 1, 2, 5}

myset.add(120)


print(myset)


myset.remove("ana")

print(myset)

numbers = {1, 10, 100}
names = {"nika", "beka", "gio"}

numbers_names = numbers.union(names)

print(numbers_names)

