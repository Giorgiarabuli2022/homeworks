# def luck_check(string):
#     str = []
#         if len(string) % 2 = 1:
#             mylistlen = len(string) + 0.5
#             for i in string:
#                 str.append(i)
#                 if i == string[mylistlen]:
#                     str.pop()
#             mylistnum = len(str)/2
#             import random
#             i = mylistnum * 2 - 1
#             for element in range(10000): 
#                 int(str[random.randit(0, mylistnum)]) + int(str[random.randit(0, mylistnum)]) + int(str[random.randit(0, mylistnum)]) = int(str[random.randit(0, mylistnum)]) + int(str[random.randit(0, mylistnum)]) = int(str[random.randit(0, mylistnum)])




# print("hello")


def find_outlier(integers):
    mylistint = []
    two = []
    odd = []
    for i in integers:            
        mylistint.append(int(i))
    for i in mylistint:
        if i % 2 == 0:
            two.append(i)
        elif i % 2 == 1:
            odd.append(i)
    if len(two) == 1:
        num = int()
        for i in two:
            num += int(i)
        return(num)
    elif len(odd) == 1:
        num = int()
        for i in odd:
            num += int(i)
        return(num) 

find_outlier([2, 4, 6, 8, 10, 3])


# def unique_in_order(iterable):
#     mylist = []
#     for i in iterable:
#         mylist.append(i)
#     set(mylist)
    
#     set(mylist)
#     list(mylist).sort()
#     print(set(mylist)) 

def make_negative( number ):
    myint = "-"
    if str(number)[0] == "-":
        return number
    elif str(number)[0] > 0:
        for i in str(number):
            myint += i
        return myint
    else:
        return 0
    
        
make_negative(99)

/**
def dot(n,m):
    a = "+---+"

*/



