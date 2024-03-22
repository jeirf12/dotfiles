from turtle import *

a = 0
b = 0

bgcolor("black")
speed(0)
pencolor("green")
penup()
goto(0, 200)
pendown()
hideturtle()

while True:
    forward(a)
    right(b)
    a+=3
    b+=1
    if b == 200: break

exitonclick()
