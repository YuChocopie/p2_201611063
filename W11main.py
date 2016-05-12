import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.penup()
t2.goto(50,50)
t2.pendown()
t2.fd(100)

def k1():
     t1.fd(50)
def k2():
     t1.back(50)
def k3():
     t1.right(45)
def k4():
     t1.left(45)
def addkeys():
     wn.onkey(k1,"Up")
     wn.onkey(k2,"Down") 
     wn.onkey(k3,"Right")
     wn.onkey(k4,"Left")

def mousegoto(x,y):
     t1.setpos(x,y)
     t1.pos()=(x,y)
     if45<x<150 and 45<y<55:
           print "Correct"

def addmouse():
     wn.onclick(mousegoto)

wn.onclick(mousegoto)



addkeys()
addmouse()
wn.listen()
turtle.mainloop()

