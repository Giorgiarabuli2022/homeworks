# საცხობი
საჭმელები = ["hot dog", "cheese cake", "meat bleans", "potato pasty"]

მენიუ = {"hot dog" : "10 ლარი",
         "cheese cake" : "15 ლარი",
         "potato bleans ( ერთი ცალი )" : "2 ლარი",
         "potato pasty" : "5 ლარი"


        }



ფასები = {"hot dog" : 10,
          "cheese cake" : 15,
          "meat bleans" : 2,
          "potato pasty" : 5
         }




print(""" Hello to our restouran "georgia" """)
print("what do you want today")
print("meniu :", მენიუ)



print("please write product you want in frame bellow")
product = input("")
print("please write quantity of product you choose in frame bellow")
quantity = int(input(""))


if product in საჭმელები:
    print("yes we have product you choose do you want to buy")
    yes = input("")
else:
    product in საჭმელები == False
    print("unfortunately we have not product you choose. do you want to buy other thing ?")
    no = input("")


if yes == "yes" or "yes of course":
    print("your price is ", ფასები[product] * quantity)
    print("do you want to buy it ?")
    yes2 = input("")
else:
    yes == "no"
    print("do you want to buy something else")
    yes_no = input("")


if no == "no":
    print("okey bye")
    input("")
else:
    no == "yes"
    print("please write product you want in frame bellow")
    product = input("")
    print("please write quantity of product you choose in frame bellow")
    quantity = int(input(""))


if  yes2 == "yes":
    print("okey bye")
else: 
    yes2 == "no"
    print("okey do you want to buy something else")
    yes3 = input("")

if yes3 == "no":
    print("okey bey")
else:
    yes3 == "yes"
    print("please write product you want in frame bellow")
    product = input("")
print("please write quantity of product you choose in frame bellow")
quantity = int(input(""))

    