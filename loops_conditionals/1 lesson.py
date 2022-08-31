''' ### conditional ###
#  if,   else,  elif

from pickle import TRUE


n = 10

George_Arabuli_is_pro = True
George_is_real_name = True
incorrect_name = ["g", "i", "o","r", "g", "e"]

if n % 2 ==0:
    print("ეს რიცხვი არის ლუწი")
else:
    print("ეს რიცხვი არის კენტი")

if n == int:
    print("n = int მონაცემი")
else:
    print("n არ არის int მონაცემი")


n = ["car", "name", "ship", "surnename"]

if len(n) == 1:
    print("n - ში არის 1 მონაცემი შეტანილი")
else:
    print("n - ში არ არის 1 მონაცემი შეტანილი")


n = ("hello world")
if n[0] == "h":
    print("hello world - ის პირველი ასოა h")
else:
    print("hello world - ის პირველი ასო არ არის h")







if George_Arabuli_is_pro == True:
    print("Andria Arabuli is noob")
else:
    print("George Arabuli is noob")


if George_is_real_name == True:
    incorrect_name[1] = "e" 
    correct_name = "".join(incorrect_name)
    big_correct_name = correct_name.capitalize()
    print(big_correct_name)
else:
    incorrect_name[1] = "i"
    correct_name = "".join(incorrect_name)
    big_correct_name = correct_name.capitalize()
    print(big_correct_name) '''





# computere_best_games = ["sim city", "fortnite", "minecraft", "nulls brawl", "roblox", "ultimate ninja shtorm 4", "fifa", "sim city buildit"]
# sim_city_is_best_game = True
# minecraft_is_second_best_game = True
# ultimate_ninja_shtorm_is_third_best_game = True
# fortnite_is_fourth_best_game = True
# roblox_is_fifth_best_game = True
# fifa_is_sixth_best_game = True
# sim_city_buildit_is_seventh_best_game = True

# ''' if sim_city_is_best_game == True:
#     print("sim city is best game")
# elif minecraft_is_second_best_game == True:
#     print("minecraft is second best game")
# else:
#      fortnite_is_fourth_best_game == True
#      print("fortnite is fourth best game")


# from turtle import speed
# speed(100)
''' number_1 = 1
number_2 = 101
while number_1**0 > number_2:
    print(number_1)
    number_1 = number_1 + 1 '''







my_name = "george"
my_age = 11
my_family_members_names = ["andrew", "george", "ia", "aleksandre"]
my_toy_cars = ["lamborjin", "beemve", "mersedes", "bigati", "toiota", "audi"]

# capitalize
my_name = my_name.capitalize()

''' 
print(my_toy_cars)
print(my_name)
print(my_family_members_names)
print(my_age)

 my_toy_cars = ", ".join(my_toy_cars)
my_family_members_names = ", ".join(my_family_members_names)
print("my name is", my_name, "i am", my_age, "years old", "my family members names are:", my_family_members_names, "my toy cars are:", my_toy_cars) '''

'''if my_family_members_names[3] == "aleksandre":
    my_family_members_names[3] = "aleqsandre"
    my_family_members_names[3] = my_family_members_names.capitalize()
    print(my_family_members_names[3])

else:
     my_family_members_names[3] = "Aleqsandre"
     my_family_members_names[3] = "Aleqsandre".lower()
 '''


my_str = "nika 6 keshelava"
print(my_str[5])


my_str = "nika 15 keshelava"
print(my_str[5]+my_str[6])

my_str = "nika 11 keshelava"
print(int(my_str[5]) + int(my_str[6]) + int("13"))
