import random
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.shape("turtle")
def k1():
    t2.forward(15)
def k2():
    t2.left(15)
def k3():
    t2.right(15)
def k4():
    t2.back(15)

wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(k4, "Down")
wn.listen()

t2.shape("turtle")
t1.shape("turtle")
t1.pencolor("green")
t2.color("pink")
t2.pencolor("black")
stopper = 0
t1.speed=1
t2.speed=5
t1.penup()
while True: 
    r1=random.randrange(1,50)
    r2=random.randrange(0,360)
    t1.fd(r1)
    t1.setheading(r2)
    stopper += 1
    if (stopper >= 1000):
        break
if  t1.pos()==t2.pos():
    t1.pencolor("red")
    t2.pencolor("red")
else:
    print"Game over"
raw_input()