import random
import turtle
import time
import math
global add
wn=turtle.Screen()

t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t1.pencolor("green")
t2.color("pink")
t2.pencolor("black")
t3.color("tan")
t3.pencolor("violet")
t1.setpos(40,40)

t1.speed=1
t2.speed=50
t1.penup()
stopper = 0
add=0

import math
def isInCircle(center,radius,pos):
    return 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius

def circle(pos,size,color):
    t3.penup()
    t3.setpos(pos)
    t3.pendown()
    t3.setheading(0)
    t3.fillcolor(color)
    t3.begin_fill()
    t3.circle(size)
    t3.end_fill()
    

def gu((x,y),color):
    t3.penup()
    t3.pencolor(color)
    t3.goto(x,y-10)
    t3.pendown()
    t3.setheading(0)
    t3.fd(40)
    t3.right(90)
    t3.fd(40)
    t3.penup()
    t3.goto(x+50,y)
    t3.pendown()
    t3.fd(30)
    t3.right(90)
    t3.fd(10)
    t3.back(10)
    t3.left(90)
    t3.fd(30)

def bok((x,y),color):
    t3.penup()
    t3.pencolor(color)
    t3.goto(x,y)
    t3.pendown()
    t3.setheading(0)
    t3.right(90)
    t3.fd(30)
    t3.left(90)
    t3.fd(50)
    t3.left(90)
    t3.fd(30)
    t3.back(15)
    t3.left(90)
    t3.fd(50)
    t3.left(90)
    t3.penup()
    t3.fd(20)
    t3.pendown()
    t3.left(90)
    t3.fd(25)
    t3.right(90)
    t3.fd(10)
    t3.back(10)
    t3.left(90)
    t3.fd(25)
    t3.right(90)
    t3.penup()
    t3.fd(20)
    t3.pendown()
    t3.back(10)
    t3.right(90)
    t3.fd(50)

def lee((x,y),color):
    t3.penup()
    t3.pencolor(color)
    t3.goto(x+10,y-55)
    t3.pendown()
    t3.setheading(0)
    t3.circle(25)
    t3.penup()
    t3.goto(x+50,y)
    t3.right(90)
    t3.pendown()
    t3.fd(70)

def job((x,y),color):
    t3.penup()
    t3.pencolor(color)
    t3.goto(x,y-10)
    t3.pendown()
    t3.setheading(0)
    t3.fd(20)
    t3.right(45)
    t3.fd(30)
    t3.back(30)
    t3.right(90)
    t3.fd(30)
    t3.back(30)
    t3.right(225)
    t3.fd(20)
    t3.penup()
    t3.goto(x+50,y-20)
    t3.pendown()
    t3.setheading(0)
    t3.fd(15)
    t3.back(15)
    t3.right(90)
    t3.fd(20)
    t3.back(40)
    t3.penup()
    t3.goto(x+8,y-47)
    t3.pendown()
    t3.setheading(0)
    t3.right(90)
    t3.fd(20)
    t3.right(270)
    t3.fd(40)
    t3.left(90)
    t3.fd(20)
    t3.back(10)
    t3.left(90)
    t3.fd(40)

def gi((x,y),color):
    t3.penup()
    t3.pencolor(color)
    t3.goto(x,y-10)
    t3.pendown()
    t3.setheading(0)
    t3.fd(40)
    t3.right(90)
    t3.fd(40)
    t3.penup()
    t3.goto(x+55,y)
    t3.pendown()
    t3.fd(60)

gu((-200,-100),"red")
bok((-100,-100),"blue")
lee((0,-100),'orange')
job((100,-100),'orchid')
gi((190,-100),'orchid')

t3.penup()
t3.goto(0,0)
t3.pendown()

def k1():
    pos1=t1.pos()
    pos2=t2.pos()
    pos3=t3.pos()
    t2.forward(15)
def k2():
    t2.left(30)
def k3():
    t2.right(30)
def k4():
    pos1=t1.pos()
    pos2=t2.pos()
    pos3=t3.pos()
    t2.back(15)

def mousegoto(x,y):
    pos1=t1.pos()
    pos2=t2.pos()
    pos3=t3.pos()
    t1.setpos(x,y)
       
def key():
    wn.onkey(k1, "Up")
    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right")
    wn.onkey(k4, "Down")
    wn.onclick(mousegoto)
       
def gamePlay():
    key()
    wn.listen()

def lab11():
    gamePlay()
    
lab11()


while True:
    pos2=t2.pos()
    pos1=t1.pos()
    pos3=t3.pos()
    r1=random.randrange(10,50)
    r2=random.randrange(0,360)
    t1.fd(r1)
    t1.right(r2)
    stopper += 1
    if (stopper>= 100):
        break
    if isInCircle(pos1,10,pos2) and pos3==(0,0) :
        circle((-200,100),50,"cyan")
	add=add+1 
	print add 
    if isInCircle(pos1,10,pos2) and isInCircle((-200,100),10,pos3) and add<=5:
        circle((-100,100),50,"blue")
	add=add+1 
	print add 
    if isInCircle(pos1,10,pos2) and isInCircle((-100,100),10,pos3) and add<=5:
	add=add+1 
	print add 
	circle((0,100),50,"green")    
    if isInCircle(pos1,10,pos2) and isInCircle((0,100),10,pos3) and add<=5:
	add=add+1 
	print add 
        circle((100,100),50,"violet")
    if isInCircle(pos1,10,pos2) and isInCircle((100,100),10,pos3) and add<=5:
	add=add+1 
	print add 
        circle((200,100),50,"black")
    if isInCircle(pos1,10,pos2) and isInCircle((200,100),10,pos3) and add<=6:       
	add=add+1 
	print add 
	circle((-200,100),50,"tan")
    if isInCircle(pos1,10,pos2) and isInCircle((-200,100),10,pos3) and 5<add<=10:
       	add=add+1  
        circle((-100,100),50,"yellow")
	print add 
    if isInCircle(pos1,10,pos2) and isInCircle((-100,100),10,pos3) and 5<add<=10:
	add=add+1 
	print add 
	circle((0,100),50,"orange")    
    if isInCircle(pos1,10,pos2) and isInCircle((0,100),10,pos3) and 5<add<=11:
	add=add+1 
	print add 
        circle((100,100),50,"pink")
    if isInCircle(pos1,10,pos2) and isInCircle((100,100),10,pos3) and 5<add<=11:
	add=add+1 
	print add 
        circle((200,100),50,"red")
    if isInCircle(pos1,10,pos2) and isInCircle((200,100),10,pos3) and 7<add<=11:     
	add=add+1 
	print add 
	circle((-200,100),50,"black")
    if isInCircle(pos1,10,pos2) and isInCircle((-200,100),10,pos3) and 11<add:
        circle((-100,100),50,"green")
	add=add+1 
	print add 
    if isInCircle(pos1,10,pos2) and isInCircle((-100,100),10,pos3) and 11<add:
	add=add+1 
	print add 
	circle((0,100),50,"cyan")    
    if isInCircle(pos1,10,pos2) and isInCircle((0,100),10,pos3) and 11<add:
	add=add+1 
	print add 
        circle((100,100),50,"violet")
    if isInCircle(pos1,10,pos2) and isInCircle((100,100),10,pos3) and 11<add:
	add=add+1 
	print add 
        circle((200,100),50,"blue")
    if isInCircle(pos1,10,pos2) and isInCircle((200,100),10,pos3) and 11<add:     
	add=add+1 
	print add 
	circle((-200,100),50,"pink")

if add==50:
    t1.pencolor("green")
    t2.pencolor("green")
else:
    t1.pencolor("red")
    t2.pencolor("red")
    print"Game over"
    print"Score"
    print add

played=open('score.txt','a')
if add>=0:
    name = raw_input("Put in your name: ")
    msg='played {0}'.format(name + '\t' + time.strftime('%Y.%m.%d , %H:%M:%S'))
    print "End Game"+'\n'+'Score' + '\t'+ str(add) +'\t' + msg
    played.write('\n' + 'Score' + '\t'+ str(add) +'\t' + msg)
    played.close()
    print "Click Screen"


wn.exitonclick()