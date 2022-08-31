# def minus(a, b):
#     for i in range(b):
#         a -= 1
#         if i == b:
#             break
#     print(a)  



# minus(10, 5)

''' 
def plus(a, b):
    for i in range(b):
        a += 1
        if i == b:
            break
    print(a) 


plus(10, 20) '''


''' def წრის_პერიმეტრი(რადიუსი):
    print(რადიუსი**2 * 3.14)

წრის_პერიმეტრი(2.7) '''


# def საშუალო_სიჩქარე(მანძილი, დრო):
#     print(მანძილი/დრო)



# def სამკუთხედის_ფართობი(ფუძე, სიგრძე):
#     print((ფუძე*სიგრძე)/2)


''' def is_isogram(string):
    z = ""
    for x in range(string):
        z.append(x)
        z.lower()
        if 2 * "a" or 2 * "b" or 2 * "c" or 2 * "d" or 2 * "e" or 2 * "f" or 2 * "g" or 2 * "h" or 2 * "i" or 2 * "j" or 2 * "k" or 2 * "l" or 2 * "m" or 2 * "n" or 2 * "o" or 2 * "p" or 2 * "q" or 2 * "r" or 2 * "s" or 2 * "t" or 2 * "u" or 2 * "v" or 2 * "w" or 2 * "x" or 2 * "y" or 2 * "z":
            print("false")
        else:
            print("true")









is_isogram("hello") '''


# def repeat_str(repiate, string):
#     x = len(string)
#     final = [""]
#     while len(string) < repiate*x:
#         final.append(string)
#         new_final = "".join(final)
#     return new_final


# repeat_str(4, "h")


# print("aa")


# def avejis_gadatanis_servisi(simzime, gadatanakm_shi):

#     fasi = (simzime*gadatanakm_shi)/150 + 40
#     print("თქვენი გადასახადია", fasi, "ლარი")

# print("kg: ") 
# i = int(input(""))
# print("m: ")  
# a = int(input(""))

# avejis_gadatanis_servisi(i, a) 






# mywords = ["hello", "goodbie", "dog",  "cat"]
# theirtrans={
#     "hello" : "გამარჯობა" "სალამი" "მისალმება",
#     "goodbie" : "ნახვამდის" "მშვიდობით" "კარგად იყავით",
#     "dog" : "ძაღლი",
#     "cat" : "კატა"
# }

# georgewords = {
#     "კატა":"cat",
#     "ძაღლი": "dog",
#     "ნახვამდის":"goodbie",
#     "გამარჯობა":"hello0"
# }

# def translate(a):
#     if a in georgewords:
#         print(georgewords[a])
#     else: a in theirtrans
#     print(theirtrans[a])
            
    


# word = input("")

# translate(word)


# def riddle_1(a, b):
#     if a > b:
#         print(a, "მეტია", b, "ზე", a/b, "ჯერ")
#     else:
#         b > a
#         print(a, "ნაკლებია", b, "ზე", b/a, "ჯერ")

# riddle_1(10, 100)


# import random 
# my_list = []
# for i in range(15):
#     my_list.append(random.randint(1, 100))
# for i in my_list:
#     if i % 3 == 0:
#         print(i)
        
# def procedure(number):

# def get_count(sentence):
#     a = sentence.count("a")
#     e = sentence.count("e")
#     i = sentence.count("i")
#     o = sentence.count("o")
#     u = sentence.count("u")
#     print(a + e + i + o + u)
    

# def duplicate_encode(word):
#     war = []
#     word_2 = word.lower()
#     x = 0
#     while x == len(word) == False:
#         count_1 = word.count(word[x])
#         if count_1 > 1:
#             war + "("
#         elif count_1 == 1:
#             war.append(")")
#     return war 

# duplicate_encode("hello")



'''komarovis amocanebi'''
# 1
# dad = 62
# son = 36
# x = (dad/2 - 1.5 * son)*-1
# print(x)


# 2
# def mycode(a, b):
#     print((b+a+1) * (b/2)) 

# mycode(0, 5)


# 3
# def sabcifri(a, b):
#     a  = (b+a+1) * (b/2)
#     str(a)
#     print(str(a)[-3])


# sabcifri(0, 1)

# 4
# def ways(a, b, c, d, e, v):
#     print(a*b*c*d*e*v)

# ways(20, 6, 7, 1, 1, 1)
 
# 5

# def speed(მანძილი, დრო, პირველისსიჩქარე, მეორესსიჩქარე, საპანერთ):
#     if საპანერთ == "საპირისპირო":
#         print(მანძილი + დრო*პირველისსიჩქარე + დრო*მეორესსიჩქარე)
#     else: 
#         საპანერთ == "ერთად"
#         print((მანძილი - დრო*პირველისსიჩქარე - დრო*მეორესსიჩქარე)**2/(მანძილი - დრო*პირველისსიჩქარე - დრო*მეორესსიჩქარე)) 
        

# speed(200, 2, 20, 20, "ერთად")

# 6

# def lokokina(სიღრმე, ადის, ჩადის):
#     print(სიღრმე - ადის + 1)

# lokokina(20, 5, 4)
'''# 7'''


print(0/0)