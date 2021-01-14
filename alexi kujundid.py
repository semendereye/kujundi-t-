#Alexandr Klis
#kujundid 8, 15, 1
#14.01.21
import turtle
import math
aken = turtle.Screen()
aken.setup(600,600)
aken.title("Alexandr Klis - kujundi töö")


#kuju 1

m=turtle.Turtle()
for i in range(4):
    m.fd(100)
    m.lt(90)
    m.fd(100)
    m.rt(90)
    m.fd(100)
    m.lt(90)





#kujund 15
def maja():
    l = turtle.Turtle()
    a=200
    for i in range(4):
        l.fd(a)
        l.lt(90)
        l.fd(a)
    l.up()
    l.fd(75)
    l.lt(90)
    l.down()
    l.color("red")
    l.fd(150)
    l.lt(90)
    l.fd(150)
    l.lt(90)
    l.fd(150)
    l.up()
    l.rt(90)
    l.fd(125)
    l.rt(90)
    l.fd(a*2)
    l.down()
    l.color("green")
    l.rt(45)
    l.fd(284)
    l.rt(90)
    l.fd(284)





def ruut():
    #kujund 8
    k= turtle.Turtle()
    a = 100
    b= a*math.sqrt(2)
    for i in range(4):
        k.fd(100)
        k.rt(45)
        k.fd(b)
        k.lt(90)
        k.fd(b)
        k.rt(45)
        k.fd(100)
        k.lt(90)
        

maja()
ruut()
    