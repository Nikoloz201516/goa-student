from turtle import*
shape("turtle")
width(5)
color("red")
begin_fill()
left(90)
forward(200)

right(90)
forward(350)

right(90)
forward(200)

right(90)
forward(350)
end_fill()
#wall making
#starting roof soon
color("yellow")
begin_fill()
penup()
goto(350, 200)
pendown()
right(45)
forward(100)
left(45)
forward(211)
left(45)
forward(100)
left(90)
end_fill()
#roof ended 
#starting door
penup()
goto(200, 0)
pendown()
begin_fill()
color ("green")
left(135)
forward(85)
right(90)
forward(45)
right(90)
forward(85)
end_fill()
#starting window
penup()
goto(110, 70 )
begin_fill()
color ("blue")
pendown()
right(90)
forward(60)
right(90)
forward(70)
right(90)
forward(60)
right(90)
forward(70)
end_fill()

#sacend window
begin_fill()
color("blue")
speed(65)
penup()
goto(310, 70)
pendown()
right(90)
forward(45)
right(90)
forward(65)
right(90)
forward(45)
right(90)
forward(65)
end_fill()


exitonclick()