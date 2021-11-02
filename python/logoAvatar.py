#! python
import turtle
from math import e

#Dibuja un espiral dando el tamaño de cada linea y sus veces dibujandolo
def spiral(size, n):
    for i in range(n):
        myPen.forward(i + (size * 2))
        myPen.right(22)

#Dibuja un espiral dando el tamaño de cada linea y sus veces dibujandolo 
#(utilizado en el logo de agua)
def spiralWater(size, n):
    for i in range(n):
        myPen.forward(i + (size * 2))
        myPen.left(25)

#Dibuja lineas curveadas fijando un tamaño y sus grados de position
def curve(size, heading):
    curveLeft(size, heading, 3)
    heading = myPen.heading()
    curveRight(size, heading, 4)

def curveFire(size, heading):
    curveRight(size, heading, 4)
    heading = myPen.heading()
    curveLeft(size, heading, 6)

def curveFireSpecial(size, heading):
    curveRight(size, heading, 6)
    heading = myPen.heading()
    curveLeft(size, heading, 4)

def curveRight(size, heading, n):
    myPen.setheading(heading)
    for i in range(n):
        myPen.forward(size)
        myPen.right(18)

def curveLeft(size, heading, n):
    myPen.setheading(heading)
    for i in range(n):
        myPen.forward(size)
        myPen.left(18)

#Dibuja un marco, fijando su tamaño de cada lado y sus repectiva posicion a dibujar
# (coordenadas height = y, width = x)
def frame(size, height, width):
    myPen.penup()
    myPen.goto(width, height)
    myPen.right(180)
    myPen.pendown()
    myPen.color('#9B9B9B')
    myPen.begin_fill()
    for i in range(4):
        myPen.forward(size)
        myPen.right(90)
    myPen.end_fill()

#Método donde se dibuja el logo de aire
def drawAir():
    myPen.penup()
    myPen.goto(-340, -120)
    myPen.setheading(0)
    myPen.pendown()
    spiral(1, 35)
    myPen.penup()
    myPen.goto(-200, -120)
    myPen.pendown()
    myPen.setheading(230)
    spiral(1, 35)
    myPen.penup()
    myPen.goto(-275, -255)
    myPen.pendown()
    myPen.setheading(110)
    spiral(1, 35)

#Método donde se dibuja el logo de agua
def drawWater():
    myPen.penup()
    myPen.goto(-275, 340)
    myPen.setheading(180)
    myPen.pendown()
    myPen.circle(150)
    myPen.penup()
    myPen.goto(-134.05, 138.70)
    myPen.pendown()
    curve(34, 177)
    myPen.penup()
    myPen.goto(-125.00, 190.00)
    myPen.pendown()
    curve(42, 177)
    myPen.penup()
    myPen.goto(-134.05, 241.30)
    myPen.pendown()
    curve(44, 177)
    myPen.penup()
    myPen.goto(-370, 200)
    myPen.setheading(300)
    myPen.pendown()
    spiralWater(0.5, 26)
    myPen.penup()
    myPen.goto(-302, 266)
    myPen.setheading(320)
    myPen.pendown()
    spiralWater(1, 25)
    myPen.penup()
    myPen.goto(-228, 293)
    myPen.setheading(410)
    myPen.pendown()
    spiralWater(0.5, 18)

#Método donde se dibuja la segunda parte del logo de tierra
def figurEarth():
    myPen.setheading(0)
    myPen.forward(100)
    myPen.left(295)
    myPen.forward(200)
    myPen.right(25)
    myPen.forward(60)
    myPen.left(270)
    myPen.forward(120)
    myPen.right(90)
    myPen.forward(60)
    myPen.right(-270)
    myPen.forward(90)
    myPen.penup()
    myPen.goto(250.52,102.74)
    myPen.pendown()
    myPen.forward(90)
    myPen.penup()
    myPen.goto(186, 314)
    myPen.pendown()
    myPen.setheading(180)
    myPen.right(295)
    myPen.forward(200)
    myPen.left(25)
    myPen.forward(60)
    myPen.right(270)
    myPen.forward(120)
    myPen.left(90)
    myPen.forward(60)
    myPen.left(-270)
    myPen.forward(90)
    myPen.penup()
    myPen.goto(221.48,102.74)
    myPen.pendown()
    myPen.forward(90)
    myPen.penup()
    myPen.goto(248, 228)
    myPen.pendown()
    myPen.setheading(380)
    spiralWater(1, 30)

#Método donde se fija la posición del logo de tierra
def drawEarth():
    myPen.penup()
    myPen.goto(186, 314)
    myPen.pendown()
    figurEarth()

def drawFire():
    myPen.penup()
    myPen.goto(226, -224)
    myPen.pendown()
    myPen.setheading(380)
    spiralWater(1, 34)
    curveFire(16, 135)
    curveFire(16, 275)
    myPen.penup()
    myPen.goto(220, -166)
    myPen.pendown()
    curveFireSpecial(11, 140)
    myPen.penup()
    myPen.goto(116, -286)
    myPen.pendown()
    curveRight(15, 154, 6)
    curveLeft(15, myPen.heading(), 6)
    curveRight(18, 366, 6)
    myPen.penup()
    myPen.goto(320, -286)
    myPen.pendown()
    curveLeft(20, 16, 7)
    curveRight(26, 114, 4)
    curveLeft(30, 195, 4)
    myPen.penup()
    myPen.goto(320, -126)
    myPen.pendown()
    curveLeft(18, 258, 3)
    curveRight(34, 288, 11)
    curveRight(14, 96, 3)
    curveLeft(12, 78, 2)

#Es el método por defecto o inicial antes de dibujar los logos
def startDefault():
    global myPen
    global window
    myPen = turtle.Turtle()
    window = turtle.Screen()
    myPen.shape('turtle')
    #Aqui se puede ajustar la velocidad con la que dibuja
    myPen.speed(0)
    turtle.bgcolor('black')
    #Dibuja los cuadros donde se van a ubicar cada logotipo
    frame(350, 15, -100)
    frame(350, 365, 60)
    frame(350, -360, -100)
    frame(350, -10, 60)
    myPen.color('#000000')
    myPen.pensize(18)
    myPen.hideturtle()

def main():
    #Inicializacion de turtle y componente de base
    startDefault()
    #Dibuja el logo de aire
    drawAir()
    #Dibuja el logo de agua
    drawWater()
    #Dibuja el logo de tierra
    drawEarth()
    #Dibuja el logo de fuego
    drawFire()
    #Permite cerrar la ejecución cuando termine, con un click
    window.exitonclick()

#Es la funcion principal que se ejecutara
main()
