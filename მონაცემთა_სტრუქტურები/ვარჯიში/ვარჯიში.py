from sre_constants import GROUPREF_LOC_IGNORE
from typing import List


# list
boy_names = ["george", "andrew", "nick"]
girl_names = ["helen", "jessica", "sandra"]


# upper list
names = boy_names + girl_names
print(names)

all_names = str(names)
print(all_names)

upper_all_names = all_names.upper()
print(upper_all_names)

# lower 

lower_all_names = all_names.lower()
print(lower_all_names)

# capitalize
car = ("lamborjin")
car_2 = car.capitalize()
print(car_2)
# i do not like it
car_3 = car_2.lower()
print(car_3)
# i do not like it again
car_4 = car.upper()
print(car_4)
# i like it !

# join
all_names_2 = ", ".join(names)
print(all_names_2)

#STR
str(all_names_2)
print(all_names_2)

# reset
list(all_names_2)
print(all_names_2)

#type
print(type(all_names_2))
print(type(all_names))

# index
print(all_names_2.index("g"))
print(all_names_2)

