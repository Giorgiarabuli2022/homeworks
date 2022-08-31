def price(quantity, ice_creem, species, question, brand):
    print(price = quantity * ice_creem[brand,"`s", species])
    if question == "what is the price of ice creem" or "how much is it" or "how much is it cost" or "how much does it cost":
        print(price, "dollar")

        return

ice_cream_brands = ["barambo", "gurjaani"]
ice_cream = ["vanil ice_craem", "straberry ice_craem", "chokolate ice_cream", "vanili", "straberry", "chokolate"]
ice_cream_price = {"barambo`s vanili ice cream" : 1,
                   "barambo`s straberry ice cream" : 1.5,
                   "barambo`s chokolate ice cream" : 2,
                   "gurjaani`s vanili ice cream" : 0.75,
                   "gurjaani`s chokolate ice_cream" : 1.5,
                   "gurjaani`s straberry ice_craem" : 1,
                   "barambo`s vanili" : 1,
                   "barambo`s straberry" : 1.5,
                   "barambo`s chokolate" : 2,
                   "gurjaani`s vanili" : 0.75,
                   "gurjaani`s chokolate" : 1.5,
                   "gurjaani`s straberry" : 1}



print("hello to george@ice_cream_parlour")
print("which ice cream do you want for desert")
print("write the name of the ice cream brand you choose")
brand = input("")
print("write the name of the ice cream  you choose")
species = input("")

if brand in  ice_cream_brands and species in ice_cream:
   print("we have the species of ice cream you choose")

print("write quantity of ice creams you want to buy")
quantity = int(input(""))

question = input("")

if question == (""):
    print("your price is", price)
