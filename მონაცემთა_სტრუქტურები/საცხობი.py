def foodprice(a, b, c, d, e ):
    print((c[a] + e[b]) * d)
def manyfoodprice(a, d):
    while a == "yes":
       for i in a == "yes":
           i == d
           i = i + i
           if a =="no":
               print(i)

foods = ["xaWapuri",  "lobiani"]
types = ["fenovani", "chveulebrivi"]
foodsprice = {"xaWapuri" : 5,
              "lobiani" : 4.5}
typesprice = {"fenovani" : 2,
              "chveulebrivi" : 0}

print("hello")
print("what do you want for today")
print("please write bellow the food, type and quantity you choose")
print("food:")
food = input("")
print("type:")
type2 = input("")


if food in foods and type2 in types:  # პირველი კოდის დასაწყისი
    print("we have food you choose please continue the shopping")
    print("quantity:")
    quantity = int(input(""))
    print("your price is"), foodprice(food, type2, foodsprice, quantity, typesprice), print("dollar") # fasis gageba
    
    
    print("do you want something else")  # შემდეგი პირობა
    answer = input("")
    if answer == "no":
        print("ok your price is"), foodprice(food, type2, foodsprice, quantity, typesprice), print("dollar")
    elif  answer == "yes":
          while answer == "yes":
              print("please write bellow the food, type and quantity you choose")
              print("food:")
              food = input("")
              print("type:")
              type2 = input("")


              if food in foods and type2 in types:  # პირველი კოდის დასაწყისი
                print("we have food you choose please continue the shopping")
                print("quantity:")
                quantity = int(input(""))
                print("your price is"), foodprice(food, type2, foodsprice, quantity, typesprice), print("dollar") # fasis gageba
                print("do you want something else")  # შემდეგი პირობა
                answer = input("")
                
                print(manyfoodprice(answer, foodprice(food, type2, foodsprice, quantity, typesprice)))