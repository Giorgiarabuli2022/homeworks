from turtle import *



a = 90
b = 200
c = 315

speed(100)

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
end_fill()

begin_fill()
color("skyblue")
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

penup()
right(180)
forward(760)
left(90)
forward(200)
right(90)
pendown()

begin_fill()
color("green")

penup()
left(2 * a)
forward(-200) 
pendown()      # 1. მონაკვეთის დახრა
forward(c)    # "ტოლფერდა" სამკუთხედის 1 მონაკვეთის სიგრძე
right(b - 50)      # 1. და 2. მონაკვეთს შორის შექმნილი კუთხის გრადუსული ზომა

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
forward(-240)
right(55)
forward(140)
left(180)
forward(400)
right(90)
forward(200)
pendown()

begin_fill()
color("yellow")
forward(245)
right(90)
forward(245)
right(90)
forward(245)
right(90)
forward(245)
end_fill()

penup()
left(90)
forward(1280)
left(90)
forward(600)
pendown()

begin_fill()
color("gray")
left(150)
forward(600)
right(120)
forward(600)
end_fill()


left(180)
forward(530)

begin_fill()
color("white")
left(130)
forward(70)
left(220)
forward(50)
right(240)
forward(50)
left(230)
forward(40)
right(40)
forward(95)
right(120)
forward(75)
end_fill()

penup()
forward(525)
left(60)
forward(40)
pendown()
forward(110)
left(90)



forward(100)
right(90)
forward(80)
right(90)
forward(100)
right(90)
forward(90)
right(180)
forward(215)
left(90)
forward(200)
left(90)
forward(315)
left(90)
forward(200)
right(180)
forward(180)

penup()
right(90)
forward(30)
pendown()


forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
left(90)

penup()
forward(150)
pendown()
forward(30)

left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)

penup()
forward(45)
left(90)
forward(50)
pendown()

begin_fill()
color("black")
right(90)
forward(320)
right(90)
forward(200)
right(90)
forward(320)
right(90)
forward(200)


right(180)
forward(30)


penup()
left(90)
forward(90)
pendown()

right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)

right(90)
forward(30)
right(90)
forward(60)


right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(60)

penup()
left(90)
forward(230)
pendown()

left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

left(90)
forward(30)
left(90)
forward(60)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(60)


penup()
forward(30)
right(90)


forward(140)
left(90)
left(180)


forward(120)
pendown()


right(90)

forward(100)
left(90)
forward(80)
left(90)
forward(100)











exitonclick()