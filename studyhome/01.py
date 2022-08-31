def disemvowel(string_):
    list_ = ""
    
    for i in string_:
        if (i == "a") == False and (i == "e") == False and (i == "i") == False and (i == "o") == False and (i == "u") == False and (i == "A") == False and (i == "E") == False and (i == "I") == False and (i == "O") == False and (i == "U") == False:
            list_ += (i)
        
    
            
            
    print(list_) 

disemvowel("andria")

def high_and_low(numbers):
    numbers2 = []
    new_numbers = ""
    for i in str(numbers):
        numbers2.append(int(numbers))
    numbers2.sort()
    new_numbers += numbers2[0]
    new_numbers += " "
    new_numbers += numbers2[-1]
    print(new_numbers) 

high_and_low([233, 43, 3524, 52255]

)

x = " 547 6 546  88"
print(int(x))

def dont_give_me_five(start,end):
    a = []
    numbers = []
    for i in range(start, end + 1):
        if "5" in str(i):
            a.append("z")
        else:
            numbers.append(str(i))
    
    print(len(numbers))
            
      

dont_give_me_five(4, 17)

def square_digits(num):
    numbers = ""
    for i in str(num):
        numbers += str(int(i)**2)
    return numbers

square_digits(556)


from numpy import character, spacing


def filter_list(l):
    number = []
    for element in l:
        if type(element) == int:
            list(number).append(element)

    print(number)


filter_list([1, "6553", 3, "GT"])



def maskify(cc):
    last_four = ""
    len1 = len(cc)
    newlen = len1 - 4

    if len(cc)<4 or len(cc) == 4:
        return cc 
    else:
        last_four += newlen * "#"
        last_four += cc[-4]
        last_four += cc[-3]
        last_four += cc[-2]
        last_four += cc[-1]
    print(last_four)



maskify("28029sh")


def high_and_low(numbers):
    numbers2 = []
    new_numbers = ""
    for i in str(numbers):
        numbers2.append(int(numbers))
    numbers2.sort()
    new_numbers += numbers2[0]
    new_numbers += " "
    new_numbers += numbers2[-1]
    return new_numbers

high_and_low("35")



def descending_order(num):
    number = ""
    for i in str(num):
        number += (str(i))
        int(number)
    list(number).sort()
    number_2 = "".join(number)
    number_3 = ""
    for i in number_2:
        number_3 += i
    newnumber = int(number_3)
    newnumber.sort()
    print(newnumber) 
    
descending_order(15)

def opposite(number):
    num = int("")
    for i in str(number):
        if str(i) == "-":
            num += ""
        
        
def descending_order(num):
    num2 = []
    number = ""
    for i in str(num):
        num2.append(i)
    num2.sort()
    num2.reverse()
    for i in num2:
        number += i
    print(int(number))

    
descending_order(58797432)

def delete_nth(order,max_e):
    if max_e == 1:
        myset = set(order)
        mylist = list(myset)
        print(mylist) 
    elif max_e > 1:
        mynumberlist = []
        i = 0
        x = 0
        while i < 100:
            order.count(x)
            if order.count(x) == 0:
                1 + 2
            elif order.count(x) < max_e:
                mynumberlist.append(order.count(x) * x)
            elif order.count(x) > max_e:
                mynumberlist.append(max_e * x)
                x += 1
        return mynumberlist
    

def solution(s):
    mylist = ["", "", ""]
    x = 0
    for i in s:
        mylist[x] += (i)
        if len(mylist[0]) == 2:
            x += 1
    if len(mylist[x]) < 2:
        mylist[x] += "_"
    return mylist
        
solution("hello mother")


def merge_arrays(arr1, arr2): 
    for i in arr2:
        arr1.append(i)
    arr1.sort()
    print(arr1) 
    
def merge_arrays(arr1, arr2): 
    mylist = []
    for i in arr1:
        mylist.append(i)
    for i in arr2:
        mylist.append(i)
    set(mylist)
    
    list(mylist).sort()
    print(mylist)

merge_arrays([89, 84, 51, 47, 43, 35, 24, 10, -1, -19, -45, -50, -64, -68, -75, -85, -93, -94], [-90, -73, -65, -55, -54, -43, -40, -32, -31, 19, 31, 53, 55, 59, 67, 84, 95])

mylist = [1, 3, 5]
newlist = [2,435]
for i in mylist:
    newlist.append(i)
print(newlist)


def merge_arrays(arr1, arr2): 
    mylist = []
    for i in arr1:
        mylist.append(i)
    for a in arr2:
        mylist.append(a)
    myset = set(mylist)
    mylist2 = list(myset)
    mylist2.sort()

    print(mylist2)
    
merge_arrays([131324,424242,24242,424],[131324,424242,24242,424] )


# def score(dice):
#     mylist = []
#     coin = 0
#     for i in dice:
#         mylist.append(i)
#     if mylist.count(1) == 3:
#         coin += 1000
#     if mylist.count()


def wave(people):
    x = 0
    my = ""
    for i in people:
        if i == people[x]:
            i.upper()


from hashlib import new


def likes(names):
    
    name = []
    for i in names:
        name.append(i)
    if name == []:
        a = ("no body likes it")
        print(a) 
    elif len(name) == 1:
        na1 = ""
        for i in name:
            na1 += i
        a = str(na1) + " " + "likes it"
        b = "".join(a)
        b
        print(b) 
    elif len(name) == 2:
        hello2 = []
        for i in name:
            hello2.append(i)
            hello2.append(" ")
            hello2.append("and")
            hello2.append(" ")
        hello2.pop(-1)
        
  
        hello2.pop(-1)
        aeiou = "".join(hello2)
        aeiou += "like this"

        return(aeiou)

    elif len(name) > 2:
        hello = []
        for i in name:
            if i == name[-1]:
                hello.append("and")
                hello.append(" ")
                hello.append(i)
            hello.append(i)
            hello.append(",")
            hello.append(" ")
            
                
            print(hello)
        hello.pop(-3)
        print(hello)
        hello.pop(-2)
        print(hello)

        newlist = "".join(hello)
        a = (str(newlist) + "likes it")
        print(str(a)) 


likes(["jacob", "alex"])


def likes(names):
    
    name = []
    for i in names:
        name.append(i)
    if name == []:
        a = ("no one likes this")
        return(a) 
    elif len(name) == 1:
        na1 = ""
        for i in name:
            na1 += i
        a = str(na1) + " " + "likes this"
        b = "".join(a)
        b
        print(b) 
    elif len(name) == 2:
        hello2 = []
        for i in name:
            hello2.append(i)
            hello2.append(" ")
            hello2.append("and")
            hello2.append(" ")
        hello2.pop(-1)
        hello2.pop(-1)
        aeiou = "".join(hello2)
        aeiou += "like this"
        print(aeiou)
    elif len(name) > 2:
        hello = []
        for i in name:
            hello.append(i)
            hello.append(",")
            hello.append(" ")
            if i == name[1]:
                hello.pop(-2)
                hello.append("and")
                hello.append(" ")
                hello.append(str(int(len(name)) - 2))
                hello.append(" ")
                hello.append("others like this")
                break
            
            
                
        newlist = "".join(hello)
        a = (str(newlist))
       
        print(a) 


likes(["jacob", "alex", "mark"])


def likes(names):
    
    name = []
    for i in names:
        name.append(i)
    if name == []:
        a = ("no one likes this")
        return(a) 
    elif len(name) == 1:
        na1 = ""
        for i in name:
            na1 += i
        a = str(na1) + " " + "likes this"
        b = "".join(a)
        b
        return(b) 
    elif len(name) == 2:
        hello2 = []
        for i in name:
            hello2.append(i)
            hello2.append(" ")
            hello2.append("and")
            hello2.append(" ")
        hello2.pop(-1)
        hello2.pop(-1)
        aeiou = "".join(hello2)
        aeiou += "like this"
        print(aeiou)
    elif len(name) == 3:
        hello3 = []
        for i in name:
            hello3.append(i)
            hello3.append(",")
            hello3.append(" ")
            if i == name[-2]:
                hello3.pop(-2)
                
                hello3.append("and")
                hello3.append(" ")
                hello3.append(name[-1])
                break
        hello3.append(" ")
        hello3.append("like this")
        a = "".join(hello3)
        b = str(a)
        print(b) 

        return(aeiou)
    elif len(name) > 3:
        hello = []
        for i in name:
            hello.append(i)
            hello.append(",")
            hello.append(" ")
            if i == name[1]:
                hello.pop(-2)
                hello.append("and")
                hello.append(" ")
                hello.append(str(int(len(name)) - 2))
                hello.append(" ")
                hello.append("others like this")
                break
            
                
        newlist = "".join(hello)
        a = (str(newlist))
        dv = (str(a)) 
        print(dv) 


def zeros(n):
    x = 0
    y = 0
    n = 0
    for i in range(n):
        if str(i) == str(n)[0]:
            x += n[y] * n[y+1]
        y+=1
        n += str(x).count("0")
        
        x * int(str(n)[y])
        if y == n:
            break

    n += str(x).count("0")
    print(n)
    
zeros(300000244294897420842)
    
            
from gettext import find


def find_it(seq):
    na = []
    num = []
    number = []
    th = []
    for i in seq:
        na.append(i)
    na.sort()
    print(na)
    x = 0
    for i in range(100):
        na.count(x)
        if na.count(x) == 0:
            number.append(1)
        elif na.count(x) > 0:
            num.append(x)
            num.append(na.count(x))
        x += 1
    print(num)
    y = 0
    for i in num:
        if i == (len(num)/2):
            break
        th.append(num[y])
        y += 2
    for i in th:
        if i % 2 == 1:
            a = (num[num.index(i)])
    return(a)

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
        
def capitalize_word(word):
    w = ""
    for i in word:
        w += i
    w2 = w.capitalize()
        
    print(w2) 

capitalize_word("say")

def spin_words(sentence):
    sentence2 = ""
    for i in sentence:
        sentence2 += i
    sentence2.split()
    y = 0
    for i in sentence2:
        if len(i) > 4:
            new = list[i].reverse
            hello2 = ""
            for i in new:
                hello2 += i
            print(hello2)
            sentence2[y] = hello2
            print(sentence2)
        y += 1

    word = ""
    for i in sentence2:
        word += i
    print(word)


    


i = "hello"
i[::-1]
print(i[::-1])

spin_words("helloojhiuh, and, hello")

def factorial(n):
    x = 1
    y = n
    for i in range(1, y + 1):
        x = x * i
    print(x)

factorial(2)

hello = "hello {} {}"
name = input("name: " )
surname = input("surname: " )
print(hello.format(name, surname) )

print("num1")
num1 = int(input())
print("num2")
num2 = int(input())
print("num3")
num3 = int(input())
print("num4")
num4 = int(input())

jami = num1 + num2 + num3 + num4
kvadratebi = num1**2 + num2**2 +num3**2 + num4**2

print("({} + {} + {} + {})/({} + {} + {} + {}) = {}".format(num1**2, num2**2, num3**2, num4**2, num1, num2, num3, num4, kvadratebi/jami ))
from importlib.machinery import DEBUG_BYTECODE_SUFFIXES



was = int(input("ნაჭრების რაოდ: "))
eat = int(input("შეჭამა: "))
print("{} ნაჭრიან პიცაში შეიჭამა {} ნაჭერი და დარჩა {} ნაჭერი".format(was, eat, was-eat))

სტუმრები = int(input("სტუმრების რაოდენობა: "))
ფული = int(input("გადასახადი ლარებში: "))
print("თითოეული იხდის {} ლარს".format(ფული/სტუმრები))

num1 = int(input("100-ზე დიდი რიცხვი: "))
num2 = int(input("10-სა და 20-ს შორის რომელიმე რიცხვი: "))
newnum = num1 % num2
newnum2 = num1 / num2
hello = ""
if len(str(newnum2)) == 5:
    for i in newnum2:
        if i == newnum[2]:
            break
        hello += i
        print(hello)
elif len(str(newnum2)) == 4:
    for i in newnum2:
        if i == newnum[1]:
            break
        hello += i
if num1 < 100 or num1 == 100 or num2 > 20 or num2 < 10:
    print("დებილი ხარ")
else:
    int(hello)
    print("{}-ში {} მოთავსდა {}-ჯერ და ნაშთია {}".format(num1, num2, hello, newnum))


i = "hello"
print(i[::2])


def FunctionName(i):
    hello = []
    for element in i:
        hello.append(element)
        if element == " ":
            hello.pop()
    hello.sort()
    low = hello[0]
    high = hello[-1]
    print(low, "-", high)

def FunctionName(num):
    numbers = ["", "", "", "",  "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",]
    y = 0
    for i in num:
        if i == " ":
            y+=1
        numbers[y] += i
        print(numbers)

    x = 0
    for i in numbers:
        if numbers[x] == "":
            numbers.pop(x)
        else:
            x += 1
    mynumlist = []
    for i in numbers:
        mynumlist.append(i)
    mynumlist.sort()
    print(mynumlist)
    high = mynumlist[-1]
    low = mynumlist[0]
    print(low, "-", high)
    

FunctionName("3 799 98 79 45 54 54 45 54")
        
def pig_it(text):
    mylist = [""]
    
    y = 0
    for i in text:
        
        mylist[y] += (i)
        
        if i == " ":
            mylist.append("")
            mylist[y] = mylist[y].strip()
            y += 1
    z = 0
    for i in mylist:
        if len(i) > 4:
            mylist[z] = mylist[z][::-1]
            
        z += 1
    newlist = " ".join(mylist)
        
    print(newlist)

pig_it("hello hello")

      
def pig_it(text):
    mylist = [""]
    
    y = 0
    for i in text:
        
        mylist[y] += (i)
        
        if i == " ":
            mylist.append("")
            mylist[y] = mylist[y].strip()
            y += 1
    print(mylist)


    for i in mylist:
        x = 0
        a = i[0]
        i[x] = i[x].replace(i[x], "")
        i[x] += a

    print(mylist)





pig_it("hellol hellpo")



def FunctionName(n):
    x = -1
    while x < n:
        if n == x**2:
            print(True)
            break
        else:
            print(False)
        x += 1
 
FunctionName(1)


def opposite(number):
    mylist = []
    num = ""
    for i in str(num):
        num += str(i)
    for i in str(num):
        mylist.append(int(i))
        print(mylist)
        if i == "-":
            mylist.pop()
            for i in str(num):
                mylist.append(int(i))
                if i == "-":
                    mylist.pop()
                mylist = "".join(mylist)
                mystr = int("")
                for i in mylist:
                    mystr+=i
                print(mystr)
                     



opposite(--1212121)
    


