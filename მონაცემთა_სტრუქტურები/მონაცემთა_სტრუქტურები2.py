# List – “სია”
# Set – “სიმრავლე”
# Tuple – “ტუპლი”
# Dictionary – “ლექსიკონი”


# list - ის შექმნა - mylist = [რაიმე მონაცემი]
# მაგალითი მოყვანილია ქვემოთ:
numbers = [1, 2, 3, 4]

print("მონაცემთა რაოდენობა ცვლადში ", len(numbers))
print("მეორე ინდექსზე მდებარე ცვლადი", numbers[2])
# მაგალითად
numbers[2] = 1 #მეორე ინდექსზე მდგომი რიცხვი ერთით ჩანაცვლდა"
print(numbers)

# ჩვენ სეგვიძლია ლისტს ელემენტი შემდეგი ფუნქციით დავამატოთ
numbers.append("Dato")
print(numbers)

# ჩვენ სეგვიძლია ლისტს ელემენტი შემდეგი ფუნქციით წავშალოთ
numbers.pop("ინდექსი მაგალითად", 3)
print(numbers)

# იმ შემთხვევაში, თუ გვსურს რომელიმე კონკრეტული ელემენტის წაშლა, მაგრამ არ ვიცით მისი ინდექსი, ამისათვის შეგვიძლია remove ფუნქცია გამოვიყენოთ მაგ.
fruits = ["apple", "banana", "lemon"]
fruits.remove("banana")



                                        
                                        
                                        
                                        
                                        
                                        #set - სიმრავლე
#  “დაულაგებელი” (unordered) 

# “უცვლელი” (Unchangeable) – ანუ ლისტისგან განსხვავებით სიმრავლის ელემტების შეცვლა არ შეგვიძლია, მაგრამ ახალი ელემენტების დამატება შესაძლებელია, 
# ამისათვის არსებობს add() ფუნქცია. ხოლო ელემენტის წასაშლელად .remove() ფუნქცია. 

car_color = {"red", "blue", "white", "black"}

car_color.add("purple")
car_color.remove("blue")

print(car_color)


# მონაცემების გაერთიანებ
# შეგვიძლია ლისტის მონაცემის შეცვა
names = {"Dato", "Ana"}

numbers = {1, 2}

names_numbers = names.union(numbers)

# თუ ჩვენ გვსურს მონაცემის გაძლიერება ანუ მისთვის მეორე მონაცემის შეერთება ისე რომ განა მე 3 მონაცემი 
# შეიმნას არამედ პირველ მონაცემში გაერთიანდეს ორივე და იგი გაიზარდოს"

names = {"Dato", "Ana", "giorgi"}

numbers = {1, 2, 3, 4, 5}

names.update(numbers)  






# tuple = ტუპლი
# unchangeable, orderded, allows duplicates nad different data types

tuple = (1, 2, "python", True)

# რამდენ ელემენტს შეიცავს ტუპლი
print(len(tuple))

print(tuple)

print(tuple[2])

mylist = list(tuple)
