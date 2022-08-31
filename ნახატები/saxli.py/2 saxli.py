from turtle import *

a = 90
b = 200
c = 315


speed(3)

# სამკუთხედი
width(5)

begin_fill()
color("skyblue")
forward(760)
left(90)
forward(400)
left(90)
forward(1525)
left(90)
forward(400)
left(90)
forward(1525)
right(90)
forward(200)
right(90)
forward(1525)
right(90)
forward(200)
left(180)
forward(200)
end_fill()

begin_fill()
color("green")
forward(190)
left(90)
forward(1525)
left(90)
forward(190)
left(90)
forward(1525)
end_fill()

begin_fill()
color("green")
left(2 * a)       # 1. მონაკვეთის დახრა
forward(c)    # "ტოლფერდა" სამკუთხედის 1 მონაკვეთის სიგრძე
right(b - 50)      # 1. და 2. მონაკვეთს შორის შექმნილი კუთხის გრადუსული ზომა
end_fill()

forward(b)    # 2. მონაკვეთის სიგრძე


right(a - 25)       # 2. და 3. მონაკვეთებს შორის წარმოქმნილი კუთხის გრადუსული ზომა
forward(b - 25)    # 3. მონაკვეთის სიგრძე

end_fill()

# ოთხკუთხედი

color("red")
begin_fill()
color("red")
right(a - 35)       
forward(b)  # 1. მონაკვეთის სიგრძე

right(a)    # 2. და 1. მონაკვეთებს შორის წარმოქმნილი კუთხის გრადუსული ზომა 
forward(c)  # 2. მონაკვეთის სიგრძე

right(a)    # 2. და 3. მონაკვეთებს შორის წარმოქმნილი კუთხის გრადუსული ზომა 
forward(b)  # 3. მონაკვეთის სიგრძე


right(a)    # 3. და 4. მონაკვეთებს შორის წარმოქმნილი კუთხილ გრადუსული ზომა
forward(c)
end_fill()
# ჯამში გამოდის სახლი



begin_fill()
color("purple")

right(0)
forward(c)
right(a)
forward(b)
right(a)
forward(c)
right(a)

end_fill()


forward(b)
begin_fill()
color("blue")
right(b + 70)
right(b - 50)      # ფერდის დახრილობა 1 მონაკვეთიდან

forward(b)    # ფერდის სიგრძე
right(a - 25)       # მეორე ფერდის დახრილობა პირველიდან
forward(b - 25) 

end_fill()

penup()
right(55)
forward(200)

pendown()

exitonclick()

