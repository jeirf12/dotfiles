#! python
import turtle

myPen = turtle.Turtle()
myPen.shape('turtle')
myPen.speed(3)
turtle.bgcolor('black')
myPen.color('#C0C0C0')
myPen.pensize(17)

def drawLogo():
    myPen.circle(154)
    myPen.left(90)
    myPen.penup()
    myPen.forward(150)
    myPen.pendown()
    myPen.forward(150)
    myPen.penup()
    myPen.forward(-150)
    myPen.left(120)
    myPen.pendown()
    myPen.forward(150)
    myPen.penup()
    myPen.forward(-150)
    myPen.left(120)
    myPen.pendown()
    myPen.forward(150)
    myPen.penup()
    myPen.forward(-150)
    myPen.left(120)
    myPen.hideturtle()

drawLogo()
turtle.done()
