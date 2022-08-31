from types import NoneType


def toyprice2(a, b, c):
    print(a[b] * c)

def toyprice(a, b, c):
    print(80%(a[b] * c))

def toyprice4(a, b, c, d):
    print(a[b] * c + d)

def toyprice3(a, b, c):
    (80%(a[b] * c))
toys = ["toy car", "toy princes", "bike", "puzzle", "monopoly"]
prices = {"toy car" : 15,
          "toy princes" : 10,
          "bike" : 100,
          "puzzle" : 20,
          "monopoly" : 30}




print("toy price:")
print("toy car : 15",
      "toy princes : 10",
      "bike : 100",
      "puzzle : 20",
      "monopoly : 30")

print("what do you want")
favtoy = input("")
print("how many",favtoy, "do you want")
quantity = int(input())
print("do you have cupon")
answer = input("")

if answer == "no":
    print("your price is"), toyprice2(prices, favtoy, quantity), print("dollar")
    print("do you want something else")
    answer2 = input("")
    if answer2 == "no":
        print("ok"), print("your price is"), toyprice2(prices, favtoy, quantity), print("dollar")
    else:
        answer2 == "yes"
        
    kode = toyprice3(prices, favtoy, quantity)
    
    print("what do you want")
    favtoy2 = input("")
    print("how many",favtoy2, "do you want")
    quantity2 = int(input())
    print("your price is"), toyprice4(prices, favtoy2, quantity2, kode), print("dollar")
    

elif answer == "yes":
    print("your price is"), toyprice(prices, favtoy, quantity), print("dollar")
    print("do you want something else")
    answer2 = input("")
    if answer2 == "no":
        print("ok"), print("your price is"), toyprice(prices, favtoy, quantity), print("dollar")
    else:
        answer2 == "yes"
        
    kode = toyprice(prices, favtoy, quantity)
    
    print("what do you want")
    favtoy2 = input("")
    print("how many",favtoy2, "do you want")
    quantity2 = int(input())
    print("your price is"), toyprice(prices, favtoy2, quantity2, kode), print("dollar")

