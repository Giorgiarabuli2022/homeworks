# from tkinter import S


# def find_it(seq):
#     num = []
#     for i in seq:
#         num.append(i)
#     num.sort()
#     for element in num:
#         if num.count(element) % 2 == 1:
#             return element

# def find_short(s):
#     words = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
#     wiu = []
#     y = 0
#     for i in s:
#         if i == " ":
#             wiu.append(i)
#             y += 1
#         else:
#             words[y] += i 

#     for i in words:
#         if i == "":
#             words.pop()
            
    
        
    
#     lens = []
#     for i in words:
#         if i == "":
#             wiu.append(i)
#         else:
#             lens.append(i) 
#             lens.append(len(i))
    
#     len2 = []
#     for i in lens[::-2]:
#         len2.append(i)
#     len2.sort()
#     a = len2[0]
#     return a
    
        
        


# # find_short("hhhhddh dhedhr fhefj")


# # def digital_root(n):
# #     num = []
# #     x = 0
# #     for i in str(n):
# #         num.append(int(i))
# #     for i in num:
# #         x += i
# #     y = 0  
# #     z = 0
# #     if len(str(x)) > 1:
# #         for i in str(x):
# #             y += int(i)
# #             if len(str(y)) > 1:
# #                 for i in str(x):
# #                     z += int(i)
# #                     return z
# #             else:
# #                 return y
# #     else:
# #         return x


# # # digital_root(942)

# # def digital_root(n):
# #     num = []
# #     x = 0
# #     for i in str(n):
# #         num.append(int(i))
# #     for i in num:
# #         x += i
# #     y = 0  
    
# #     if len(str(x)) == 1:
# #         return x
# #     elif len(str(x)) > 1:
# #         while len(str(y)) > 1:
# #             z = 0
# #             print(y)
# #             for i in str(y):
# #                 z += int(i)
# #             y = z
# #             if len(str(y)) == 1:
# #                 print(y) 
            
# #     else:
# #         print("z")

# # digital_root(5)

# # digital_root(7289492)


# def pig_it(text):
     
#     mylist = []
#     mystr = ""
#     myword = ""
#     for i in text:
#         mylist.append(i)
#         if i == text[0]:
#             mylist.pop()
#             myword += i
    



# def snail(snail_map):
#     mylist = []
#     if len(snail_map) == 1:
#         for i in snail_map:
            
#             for element in i:
#                 mylist.append(element)
#         print(mylist)
#         return 
#     else:
#         y = 0
#         x = 3
#         z = 0
#         for i in snail_map:
            
#             if x % 2 == 0:
#                 z = len(i)
#                 x += 1
#                 for a in i:
                    
#                     if z == -1:
#                         break
#                     mylist.append(i[z-1])
#                     z -= 1
                   
                    
 

#             else:
#                 for a in i:
#                     mylist.append(a)
#                 x += 1
#         print(mylist)
        

# snail([[2, 3, 4], [2,3,5]])

# def high_and_low(num):
#     mylist2 = []
#     mylist = [""]
#     x = 0
#     mystr = ""
#     myint = int()
#     for i in num:
#         if i == " ":
#             mylist.append("")
#             x += 1
#         else:
#             mylist[x] += i
            
    
#     for i in mylist:
#         mylist2.append(int(i))
    
#     mylist2.sort()
#     mystr += str(mylist2[-1])
#     mystr += " "
#     mystr += str(mylist2[0])
#     mystr
#     print(mystr)
# high_and_low("343 43 855 83")


# def accum(s):
#     mylist = []
#     mystr = ""
#     myint = 0
#     for i in s:
        
#         mylist.append(i.upper())
#         mylist.append(myint * i.lower())
#         mylist.append("-")
#         myint += 1
#     mylist.pop()
#     for i in mylist:
#         mystr += i
#     print(mystr)


# def get_middle(s):
#     mystr = ""
#     if len(s) % 2 == 1:
#         myint = int(len(s))/2 + 0.5
#         myint2 = myint + 1
#         mystr += s[int(myint)-1]
#         mystr += s[int(myint2)-1]
#         return mystr
#     else:
#         myint = len(s)/2
#         myint2 = myint + 1
#         mystr += s[myint-1]
#         mystr += s[myint2-1]
#         return mystr
# get_middle("g")

# def is_square(n):    
#     import random
    
   
#     if random.randint(0, 100000000000000000000000)**2 == n:
#         for i in range(1000000000000000000000000000000000000000000000000000000):
#             print(True)
#         else:
#             print(False)

# is_square(8)

mystr = "a"
myname = "andria"
if mystr in myname:
    print(myname)
else:
    print("aaa")