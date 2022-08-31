''' i = 8
while i < 14:
     i += 1
     if i == 12:
        break
     print(i)

i = "nigga"
while len(i) < 10:
   print(i)
 '''

# i = 0
# my_list = ["xinkhali", "mwvadi", "pizza", "fafa", "nayini"]
# while i < len(my_list):
#     print(my_list[i])


from fileinput import nextfile
from operator import not_
from os import read, remove
from re import I
from subprocess import BELOW_NORMAL_PRIORITY_CLASS

from setuptools import Command

my_list = ["khinkali", "mwvadi", "qababi", "fafa", "qatami"]
my_dict = {"khinkali": 1.6,
     "mwvadi" : 20,
     "qababi" : 10,
     "fafa" : 0,
     "qatami" : 30,
     "nayini" : ["shikoladis", "marwyvis", "qoqosis", "adamianis"]
 }

# print(my_dict["mwvadi"])


my_list.append("pizza")





# shezelili_sachmeli = ""
# for food in my_list:
#     shezelili_sachmeli += food 
# print(shezelili_sachmeli





# """                  "მანქანების გაყიდვა"                                        """





my_cars = {"brend" :  ["ლამბორჯინი", "ბეემვე", "მერსედესი", "ტოიოტა", "აუდი", "ნისანი"],
           "cars_color" : ["მწვანე", "ლურჯი", "წითელი", "თეთრი", "შავი", "მუქი ნაცრისფერი", "ყვითელი"],
           "ლამბორჯინი" : "ლამბორჯინის ფასი არის 20000 დოლარი",
           "ტოიოტა" : "ტოიოტა ღირს 4000 ლარი",
           "ბეემვე" : "ბეემვე ღირს 5000 დოლარი", 
           "მერსედესი" : "მერსედესი ღირს 6000 დოლარი",
           "აუდი" : "აუდი ღირს 4000 დოლარი",
           "ნისანი" : "ნისანი ღირს 3500 დოლარი"
           }





print("გამარჯობა")
print("მანქანის სახელი რომლის ყიდვაც გინდათ შეიყვანეთ ქვედა ჩარჩოში:")
fav_car = input("enter your fav car: ")
if fav_car in my_cars["brend"]:
    print("დიახ გვაქვს, გსურთ შეძენა?")
else:
    fav_car not in my_cars["brend"]
    print("სამწუხაროდ არ გვყავს, მაგრამ უახლოეს კვირაში გვეყოლება და აუცილებლად შეგატყობინებთ")
    answer0 = input("სხვა ავტომობილმაც დაგაინტერესად? ")

a = "სხვა ავტომობილმაც დაგაინტერესად? "
if  answer0 in input(a):
    fav_car = input("შეიყვანეთ თქვენ მიერ არჩეული ავტომობილი ქვედა ჩარჩოში ")
else:
    answer0 not in input(a)
    


 
print("მანქანის ფასის გასაგებად მიუთითეთ ქვემოთ თქვენ მიერ შერჩეული ავტომობილი")

car_cost = input("რა ღირს ")

if car_cost in my_cars[fav_car]:
    print(my_cars[fav_car])
else: 
    car_cost not in my_cars[fav_car]
    input("მისი ფასი ჯერ-ჯერობით უცნობია მაგრამ მალე შეგატყობინებთ")

yes_or_no = input("გსურთ შეძენა?")

if yes_or_no == "დიახ":
    color = input("რა ფერის გნებავთ? ")
else:
    yes_or_no == "არა"
    input("კარგით თუ კიდევ რამე გნებავთ შეგვატყობინეთ")



if color in my_cars["cars_color"]:
    last_answer = input("თქვენს მიერ შერჩეული ფერი არის ჩვენს მარაგში შეიძენთ ")
else:
    color not in my_cars["cars_color"]
    last_answer2 = input(color, "ფერის", fav_car, "არ არის ჩვენს მარაგში. გსურთ ფერის შეცვლა?")


if last_answer == "დიახ":
    print("შეძენა წარმატებულად დასრულდა იმედია ისიამოვნეთ ჩვენი მომსახურებით")
else:
    last_answer = "არა გმადლობთ" or "არა"
    print("მოგვწერეთ თუ კიდევ დაგჭირდებათ რამე")