import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgpic("miro.GIF")
import math
def isInCircle(center,radius,pos):
    return 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius

def circle((x,y),size):
    t1.setpos(x,y)
    t1.setheading(0)
    t1.fillcolor("yellow")
    t1.begin_fill()
    t1.circle(size)
    t1.end_fill()
def isInRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    return xs<=curpos[0]<=xe and ys<=curpos[1]<=ye
def sasasa((x,y),size):
    angle = 90
    t1.fillcolor("RED")
    t1.begin_fill()
    t1.setpos(x,y)
    t1.setheading(0)
    for i in range(4):
        t1.forward(size)
        t1.right(angle)
    t1.end_fill()

def sasa((x,y),size):
    angle = 90
    t1.setpos(x,y)
    t1.setheading(0)
    for i in range(4):
        t1.forward(size)
        t1.right(angle)

def base():
    t1.clear()
    t1.setpos(100,0)
    t1.circle(100)
    sasa((0,0),100)
    t1.penup()
    t1.goto(-200,-50)
    t1.pendown()
    t1.fd(400)
    t1.pendown()
    t1.home()

def keyup():
    pos=t1.pos()
    t1.forward(45)
    if isInRectangle((pos),[(0,-100),(100,0)]):
        sasasa((0,0),100)
    if isInCircle((100,100),100,pos):
        circle((100,0),100)

def keyleft():
    t1.left(45)

def keyright():
    t1.right(45)

def keydown():
    pos=t1.pos()
    t1.back(45)
    if isInRectangle((pos),[(0,-100),(100,0)]):
        sasasa((0,0),100)
    if isInCircle((100,100),100,pos):
        circle((100,0),100)

    
def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
     
def mousegoto(x,y):
    t1.setpos(x,y)
    pos=t1.pos()
    if isInRectangle((x,y),[(0,-100),(100,0)]):
        sasasa((0,0),100)
    if isInCircle((100,100),100,pos):
        circle((100,0),100)
    if -55<y<-45:
        t1.pencolor("red")
	t1.penup()
	t1.goto(-200,-50)
	t1.pendown()
	t1.fd(400)
	t1.penup()
	t1.home()
        t1.pendown()


def addMouse():
    wn.onclick(mousegoto)
    
def gamePlay():
    base()
    addKeys()
    addMouse()
    wn.listen()
    turtle.mainloop()


def lab11():
    gamePlay()


lab11()