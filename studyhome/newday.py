# name = "giorgi"
# surname = "arabuli"
# age = "11"
# weigh = "27kg"
# sity = "Tbilisi"
# print("i am {} {} i am {} years old my weigh is {} i live in {}".format(name, surname, age, weigh, sity))

# def is_isogram(string):
#     mystr = ""
#     mylist = []
#     myint = int()
#     mylist2 = []
#     for i in string:
#         mylist.append(i.lower())
#     for i in mylist:
#         x = mylist.count(i)  პოემა
#         mylist2.append(x)
#     for i in mylist
#         if i == 1:
#             mystr += ""
#         else:
#             myste += False
#     if len(mystr) > 0:
#         return True
#     else:
#         return False

# is_isogram('hello')

# def count_smileys(arr):
#     mylist = []
#     mystr = ""
#     myint = int()
#     for i in arr:
#         mylist.append(i)
#     for i in mylist:
#         if len(i) == 3:
#             if i[0] == ":" or i[0]:
#                 if i[1] == "-" or i[1] == "~":  
#                     if  i[2] == "D" or i[2] == "}" or i[2] == "[" or i[2] == ">":
#                         myint += 1

#         if len(i) == 2:
#             if i[0] == ":" or i[0]:
#                 if  i[1] == "D" or i[1] == "}" or i[1] == "[" or i[1] == ">":
#                     myint += 1
                
#     return myint
    

# def count_smileys(arr):
#     mylist = []
#     mystr = ""
#     myint = int()
#     for i in arr:
#         mylist.append(i)
#     for i in mylist:
#         if len(i) == 3:
#             if i[0] == ":" or i[0] == ";":
#                 if i[1] == "-" or i[1] == "~":  
#                     if  i[2] == "D" or i[2] == "}" or i[2] == "[" or i[2] == ">" or i[2] == ")":
#                         myint += 1


# x = 4
# print(x ** (1. / 2))

#         if len(i) == 2:
#             if i[0] == ":" or i[0] == ";":
#                 if  i[1] == "D" or i[1] == "}" or i[1] == "[" or i[1] == ">" or i[1] == ")": 
#                     myint += 1
#     return myint
# print(count_smileys([':~)']))



# from hashlib import new
# from random import randint
# from this import d
# from xml.dom.pulldom import default_bufsize


# /

# print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))


# mylist = [13, 5, 8, 887]
# for i in mylist[::-1]:
#     print(i)

# print(2**5)

# def format_duration(seconds):
#     myint = int()
#     mystr = ""
#     mulist = []
#     if seconds == 0:
#         return "now"
#     elif seconds < 60:
#         mystr += seconds
#         if seconds > 1:
#             mystr += str(y)
#             mystr += " "
#             mystr += "seconds"
#         else:
#             mystr += str(y)
#             mystr += " "
#             mystr += "second"

#         return mystr
#     elif seconds > 59 and seconds < 3600:
#         x = seconds // 60
#         y = seconds % 60
#         if x > 1 and y > 1:
#             mystr += str(x)
#             mystr += " "
#             mystr += "minutes"
#             mystr += " "
#             mystr += y 
#             mystr += " "
#             mystr += "seconds"
#         elif x == 1 and y > 1:
#             mystr += str(x)
#             mystr += " "
#             mystr += "minute"
#             mystr += " "
#             mystr += y 
#             mystr += " "
#             mystr += "seconds"
#         elif x == 1 and y == 1:
#             mystr += str(x)
#             mystr += " "
#             mystr += "minute"
#             mystr += " "
#             mystr += y 
#             mystr += " "
#             mystr += "second"
#         elif x > 1 and y == 1:
#             mystr += str(x)
#             mystr += " "
#             mystr += "minutes"
#             mystr += " "
#             mystr += y 
#             mystr += " "
#             mystr += "second"
#         return mystr
#     elif seconds > 3600 and seconds < 86400:
#         z = seconds // 3600
#         x = (seconds - (z * 3600)) // 60
#         y = (seconds - (z * 3600) - (y * 60))
#         if x == 0 and y == 0:
#             if z == 1:
#                 mystr += str(z)
#                 mystr += " "
#                 mystr += "hour"
#             else:
#                 mystr += str(z)
#                 mystr += " "
#                 mystr += "hours"
#         elif x == 0 and y > 0:
#             if y == 1 and z == 1:
#                 mystr += str(z)
#                 mystr += " "
#                 mystr += "hour"
#                 mystr +=  " "
#                 mystr += str(y)
#                 mystr +=  " "
#                 mystr += "second"
#             elif y > 1 and z > 1:
#                 mystr += str(z)
#                 mystr += " "
#                 mystr += "hours"
#                 mystr +=  " "
#                 mystr += str(y)
#                 mystr +=  " "
#                 mystr += "seconds"
#             elif y > 1 and z == 1:
#                 mystr += str(z)
#                 mystr += " "
#                 mystr += "hour"
#                 mystr +=  " "
#                 mystr += str(y)
#                 mystr +=  " "
#                 mystr += "seconds"
#             elif y == 1 and z > 1:
#                 mystr += str(z)
#                 mystr += " "
#                 mystr += "hours"
#                 mystr +=  " "
#                 mystr += str(y) 
#                 mystr +=  " "
#                 mystr += "second"
#             return mystr
#         elif x > 0 and y < 0:
#             if x == 1 and z == 1:
#                 mystr += str(z)
#                 mystr += " "
#                 mystr += "hour"
#                 mystr +=  " "
#                 mystr += str(x)
#                 mystr +=  " "
#                 mystr += "minute"
#             elif x > 1 and z > 1:
#                 mystr += str(z)
#                 mystr += " "
#                 mystr += "hours"
#                 mystr +=  " "
#                 mystr += str(x)
#                 mystr +=  " "
#                 mystr += "minutes"
#             elif x > 1 and z == 1:
#                 mystr += str(z)
#                 mystr += " "
#                 mystr += "hour"
#                 mystr +=  " "
#                 mystr += str(x)
#                 mystr +=  " "
#                 mystr += "minutes"
#             elif x == 1 and z > 1:
#                 mystr += str(z)
#                 mystr += " "
#                 mystr += "hours"
#                 mystr +=  " "
#                 mystr += str(x)
#                 mystr +=  " "
#                 mystr += "minute"
#             return mystr
 
            
#         else:
#             if x == 1 and y == 1 and z == 1:
#                 mystr += z
#                 mystr += " "
#                 mystr += "hour"
#                 mystr += " "
#                 mystr += x
#                 mystr += " "
#                 mystr += "minute"
#                 mystr += " "
#                 mystr += y
#                 mystr += " "
#                 mystr += "second"
#             elif x > 1 and y == 1 and z == 1:
#                 mystr += z
#                 mystr += " "
#                 mystr += "hour"
#                 mystr += " "
#                 mystr += x
#                 mystr += " "
#                 mystr += "minutes"
#                 mystr += " "
#                 mystr += y
#                 mystr += " "
#                 mystr += "second"
#             elif x == 1 and y > 1 and z == 1:
#                 mystr += z
#                 mystr += " "
#                 mystr += "hour"
#                 mystr += " "
#                 mystr += x
#                 mystr += " "
#                 mystr += "minute"
#                 mystr += " "
#                 mystr += y
#                 mystr += " "
#                 mystr += "seconds"
#             elif x == 1 and y == 1 and z > 1:
#                 mystr += z
#                 mystr += " "
#                 mystr += "hour"
#                 mystr += " "
#                 mystr += x
#                 mystr += " "
#                 mystr += "minute"
#                 mystr += " "
#                 mystr += y
#                 mystr += " "
#                 mystr += "seconds"
#             elif x > 1 and y > 1 and z == 1:
#                 mystr += z
#                 mystr += " "
#                 mystr += "hour"
#                 mystr += " "
#                 mystr += x
#                 mystr += " "
#                 mystr += "minutes"
#                 mystr += " "
#                 mystr += y
#                 mystr += " "
#                 mystr += "seconds"
#             elif x > 1 and y == 1 and z > 1:
#                 mystr += z
#                 mystr += " "
#                 mystr += "hours"
#                 mystr += " "
#                 mystr += x
#                 mystr += " "
#                 mystr += "minutes"
#                 mystr += " "
#                 mystr += y
#                 mystr += " "
#                 mystr += "second"
#             elif x == 1 and y > 1 and z > 1:
#                 mystr += z
#                 mystr += " "
#                 mystr += "hours"
#                 mystr += " "
#                 mystr += x
#                 mystr += " "
#                 mystr += "minute"
#                 mystr += " "
#                 mystr += y
#                 mystr += " "
#                 mystr += "seconds"
#             elif x > 1 and y > 1 and z > 1:
#                 mystr += z
#                 mystr += " "
#                 mystr += "hours"
#                 mystr += " "
#                 mystr += x
#                 mystr += " "
#                 mystr += "minutes"
#                 mystr += " "
#                 mystr += y
#                 mystr += " "
#                 mystr += "seconds"
#             return mystr
    
# print(3600 * 24)

# def format_duration(seconds):
    
#     year =  seconds // 31104000
    
#     month = (seconds -  year * 31104000) // 2592000 
   
#     day = (seconds - (year * 31104000 + month * 2592000)) // 86400
    
#     hour = (seconds - (year * 31104000 + month * 2592000 + day * 86400)) // 3600
    
#     min = (seconds - (year * 31104000 + month * 2592000 + day * 86400 + hour * 3600)) // 60

#     second = (seconds - (year * 31104000 + month * 2592000 + day * 86400 + hour * 3600 + min * 60)) 
#     smhdmylist = ["second", "min", "hour", "day", "month", "year"]
#     mynumlist = [second, min, hour, day, month, year]
    
#     myfinallist = []
#     myfinalstr = ""
#     myint = 0
#     for i in mynumlist:
#         if i == 0:
#             smhdmylist.pop(myint)
#             mynumlist.pop(myint)
#         elif i > 1:
#             smhdmylist[myint] = smhdmylist[myint] + "s"
        
#         myint += 1

#     myint = 0
#     for i in mynumlist:
#         if i == 0:
#             smhdmylist.pop(myint)
#             mynumlist.pop(myint)
#         elif i > 1:
#             smhdmylist[myint] = smhdmylist[myint] + "s"
        
#         myint += 1
    
#     myint = 0
#     for i in mynumlist:
#         myfinallist.append(str((mynumlist[myint])))
#         myfinallist.append(" ")
#         myfinallist.append(smhdmylist[myint])
#         myfinallist.append(" ")
#     myfinallist.pop()
#     myfinalstr = "".join(myfinallist)
#     return(myfinalstr)


# def format_duration(seconds):
    
#     year =  seconds // 31104000
    
    
   
#     day = (seconds - (year * 31104000)) // 86400
    
#     hour = (seconds - (year * 31104000 + day * 86400)) // 3600
    
#     min = (seconds - (year * 31104000 + day * 86400 + hour * 3600)) // 60

#     second = (seconds - (year * 31104000 + day * 86400 + hour * 3600 + min * 60)) 
#     smhdmylist = ["year", "day", "hour", "minute", "second"]
#     mynumlist = [year, day, hour, min, second]
    
#     myfinallist = []
#     myfinalstr = ""
#     myint = 0
#     for i in mynumlist:
#         if i == 0:
#             smhdmylist.pop(myint)
#             mynumlist.pop(myint)
        
        
#         myint += 1

#     myint = 0
#     for i in mynumlist:
#         if i == 0:
#             smhdmylist.pop(myint)
#             mynumlist.pop(myint)
       
        
#         myint += 1
#     myint = 0
#     for i in mynumlist:
#         if i == 0:
#             smhdmylist.pop(myint)
#             mynumlist.pop(myint)
#         elif i > 1:
#             smhdmylist[myint] = smhdmylist[myint] + "s"
        
#         myint += 1
    
    
#     myint = 0
#     print(mynumlist)
#     print(smhdmylist)
#     for i in mynumlist:
#         myfinallist.append(str((mynumlist[myint])))
#         myfinallist.append(" ")
#         myfinallist.append(smhdmylist[myint])
        
#         myfinallist.append(",")
#         myfinallist.append(" ")
#         myint+=1
#     myfinallist.pop()
    
#     myfinallist.pop()
#     print(myfinallist)
   
#     myfinallist[-5] = " and"
#     myfinalstr = "".join(myfinallist)
   
#     return(myfinalstr)
# def format_duration(seconds):
#     if seconds == 0:
#         return "now"
    
#     year =  seconds // 31104000
    
    
#     day = (seconds - (year * 31104000)) // 86400
    
#     hour = (seconds - (year * 31104000 + day * 86400)) // 3600
    
#     min = (seconds - (year * 31104000 + day * 86400 + hour * 3600)) // 60

#     second = (seconds - (year * 31104000 + day * 86400 + hour * 3600 + min * 60)) 
#     smhdmylist = ["year", "day", "hour", "minute", "second"]
#     mynumlist = [year, day, hour, min, second]
    
#     myfinallist = []
#     myfinalstr = ""
#     myint = 0
#     for i in mynumlist:
#         if i == 0:
#             smhdmylist.pop(myint)
#             mynumlist.pop(myint)
        
        
#         myint += 1

#     myint = 0
#     for i in mynumlist:
#         if i == 0:
#             smhdmylist.pop(myint)
#             mynumlist.pop(myint)
#         myint += 1
#     myint = 0
#     for i in mynumlist:
#         if i == 0:
#             smhdmylist.pop(myint)
#             mynumlist.pop(myint)
#         elif i > 1:
#             smhdmylist[myint] = smhdmylist[myint] + "s"
        
#         myint += 1
    
    
#     myint = 0
    
#     for i in mynumlist:
#         myfinallist.append(str((mynumlist[myint])))
#         myfinallist.append(" ")
#         myfinallist.append(smhdmylist[myint])
        
#         myfinallist.append(",")
#         myfinallist.append(" ")
#         myint+=1
#     myfinallist.pop()
    
#     myfinallist.pop()
#     if len(myfinallist) == 3:
#         myfinalstr = "".join(myfinallist)
#         return myfinalstr
#     myfinallist[-5] = " and"
#     myfinalstr = "".join(myfinallist)
#     return(myfinalstr)

# print(
# format_duration(988889989898888888888888888888888888888999999999999999999999999999999998888888888888888888888888888888889999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
# 4 years, 68 days, 3 hours and 4 minutes'

# print(25*5*25*5)
# print("zzz")if a


# def digital_root(n):
#     mynum = str(n)
#     mystr = []
#     newnum = mynum
#     x = len(newnum)
#     while x > 1:
#         newnum = 0
#         for i in list(mynum):
#             newnum += i
    
        
#     return newnum

# print(digital_root(59))

# def duplicate_count(text):
#     myset = set(text)
#     import random
#     mystr = text.lower()
#     myint = 0
#     for i in list(myset):
        
#         x = mystr.count(i)
#         if x > 1:
#             myint += 1
#     return myint

# def solution(s):
#     mylist = []
#     x = 0
#     myint = 0
#     mystr = ""
#     for i in s:
#         mystr += i
#     for i in mystr:
#         if x % 2 == 0:
#             mylist.append("")
#             mylist[myint] += i
#             myint += 1
#         else:
#             mylist[myint] += i
        
#         x += 1
#     mylist.pop()
#     if len(mylist) == 1:
#         mylist.pop()
#         mylist[-1] += "_"
#         return mylist
#     else:
#         return mylist
            


# print(solution("aefwef"))


# def reverse_words(text):
#     mylist = []
#     newlist = [""]
#     for i in text:
#         mylist.append(i)
#     myint = 0
    
#     for i in mylist:
        
#         if i == " ":
#             mylist.append(" ")
            
#         else:
#             newlist[myint] += i
        
#     mystr = ""
#     myint = 0
#     for i in newlist:
#         mystr += i
#         myint+= 1
    
#     return mystr
        
# print(reverse_words("apple 375"))

# from ast import Break
# from hashlib import new
# from inspect import modulesbyfile, signature
# from os import dup


# def words_to_marks(x):
#     z = 0
#     numberslist = []
#     alphabets_in_capital=[]
#     for i in range(65,91):
#         alphabets_in_capital.append(chr(i).lower())
        
#     print(alphabets_in_capital)
#     for i in range(1, 28):
#         numberslist.append(i)
    
#     for i in x:
#         y = alphabets_in_capital.index(i)+1
#         z += y
#     return z
   

    
# print(words_to_marks("friendship"))

# ყველაფერი commente ბშია
# def persistence(n):
#     z = n
#     print(z)
#     while len(str(z)) > 1:
#         m = list(str(z))
#         z = 1
#         print(m)
#         print(z)
#         for i in m:
#             z = z * int(i)
#             print(i)
            
#     return z


# print(persistence(36))

    
# def opposite(number):
#     myfirststr = "-"
#     mysecstr = ""
#     a = 0
   
#     if str(str(number)[0]) == "-":
#         newnum = number*-1
#         return newnum
#     else:
#         newnum = number * -1
#         return newnum

# print(opposite(-21646797))

# def pig_it(text):
#     mystr = ""
#     mylist = []
#     myint = 0
#     mynum = 0
#     for i in text:
        
#         if myint == 0:
#             mylist.append("")
#             mylist[myint]+=(i)
#             myint+=1
        
#         else:
#             mylist[myint]+=i
#             myint+=1
#     return mylist

# print(pig_it("hello boy"))

# def tower_builder(n_floors):
#     myint = -1
#     mystr = ""
#     mylist = [""]
#     mysecint = 2
#     mycode = "*"
#     newcode = " "
#     k = n_floors - 1
#     num = 0
#     for i in range(n_floors):
        
#         mylist[num]+=newcode*k
#         mylist[num] += mycode*(2+myint)
#         mylist[num] += newcode*k
#         mylist.append("")
#         num+=1
#         myint+=2
#         k -= 1
    
#     mylist.pop()
            
#     return mylist
    

# print(tower_builder(2))



# def duplicate_count(text):
#     myset = {""}
#     y = 0
#     for i in str(text).lower():
#         myset.add(i)
#     myset.remove("")
#     for i in myset:
#         x = str(text.lower()).count(str(i))
#         if x > 1:
#             y+=1



#     return y
    


# print(duplicate_count("r7SfHLrz0ib2v0fJAGGKgYOi90KhxYic5kffAiwzCjSTfM0gzUHfdu08CcejVlucVT9Gf"))

# def expanded_form(num):
#     y = "1" + (len(str(num))-1) * "0"
#     x = 1
#     myint = 0
#     mystr = ""
#     mylist = []
#     mynum1 = 0
#     for i in str(num)[::-1]:
#         if x != "0":
#             y = str(int(i)*x) 
            
#             mylist +=  y
#             mylist += " "
#             mylist += "+"
#             mylist += " "
#             x = 10 * x
#             mynum1 += 1
#         if mynum1 == len(str(num)):
#             t = y

#     mylist.pop()
#     mylist.pop()
#     mylist.pop()
#     b = mylist
#     mystr = "".join(mylist)
#     mylist = []
#     myint = 1
#     for i in mystr:
#         if i == " ":
#             myint += 1
    

#     mylist = []
#     for i in range(myint):
#         mylist.append("")
#     num = -1
#     x = ""
#     for i in mystr:
#         if i == " ":
#             mylist[num] += x
#             num -= 1
#             x = ""
#         else:
#             x += str(i)

#     z = int(y)
#     mylist[0] =  y
#     mystr3 = ""
#     mylistx = []
#     for i in mylist:
#         mylistx.append(i)
#         mylistx.append(" ")
#     mystr3 = "".join(mylistx)
#     return mystr3


# print(expanded_form(1222003))


# def tribonacci(signature, n):
#     mylist = []
#     myint = 0
#     if n < 3:
#         print("hello")
#         while len(mylist) < n:
            
#             x = int(signature[myint])
#             myint += 1
#             mylist.append(x)
#         return mylist
#     for i in signature:
#         mylist.append(i)
#     x = 0
    
#     while len(mylist) < n:
#         x = 0
#         myaaaaa = 0
#         mynewlist = mylist[::-1]
#         for i in mynewlist:
#             x += i
#             myaaaaa += 1
#             if myaaaaa == 3:
#                 break
#         mylist.append(x)

#     return mylist


# print(tribonacci([113, 172, 197], 2))



# def myfunc(sum):
#     x =0
#     for i in sum:
#         x += i
#     return x

# def to_jaden_case(string):
#     mylist = [""]
#     myint = 0
#     mylist2 = []
#     for i in string:
#         if i == " ":
#             myint += 1
#             mylist.append("")
#             mylist[myint] += i
#         else:
#             mylist[myint] += i
#     for i in mylist:
#         i[0] += i[0].upper()
#         mylist2.append(i.capitalize())
#         print(mylist2)
#         print(i.capitalize())
#     mystr = "".join(mylist2)
#     return mylist2

# print(to_jaden_case("hello my friend"))

def mynum():
    myinput = input("number1: ")
    myinput2 =  input("number2: ")
    myinput3 = input("sign: ")
    mynum1 = int(myinput)
    mynum2 = int(myinput2)
    if myinput3 == "+":
        return mynum1*mynum2
    elif myinput3 == "-":
        return mynum1-mynum2
    elif myinput3 == "*":
        return mynum2*mynum1
    else:
        return mynum1/mynum2



def myfunc()