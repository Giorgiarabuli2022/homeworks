# def square_digits(num):
#     newnum = []
#     x = 0
#     while x < len(list(num)):
#         newnum.append(int(num)[x]^2)
        
#     return newnum

# square_digits(123)

# print("hello world")
# arr = ["nika", "nika1", "nika2"]

# i = ""

# for ellement in arr:
#     for char in ellement:
#         i += char



# def card_nums(a):
#     mylist = []
#     mylist = ""
#     myint = 0
#     for i in a:
        
#         if myint == len(a)-4:
#             mylist.append(a[-4:-1])
#             mylist.append(a[-1])
#             break
#         if i == " ":
#             mylist.append(i)
#         else:
#             mylist.append("#")
#         myint += 1
        
#     for i in mylist:
#         mylist += i
#     print(mylist)
        

# card_nums("432644635241255")
        
           
# def to_weird_case(string):
#     mylist = []
#     y = 0
#     mystr = ""
#     for i in string:
#         y += 1
#         if i == " ":
#             mylist.append(i)
#             print(mylist)
#         elif y % 2 == 1:
#             mylist.append(i.upper())
#             print(mylist)
#         elif y % 2 == 0:
#             mylist.append(i)
#             print(mylist)
#     for i in mylist:        
#         mystr += i
#     print(mystr)

# to_weird_case("This is


