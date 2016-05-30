import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
import os
mydir=os.getcwd()
filename='python.txt'
myfilename=mydir +'\\'+ filename
myfilename=os.path.join(mydir,filename)
myfilehandle=open(myfilename)
myfilehandle.close()
myfilehandle=open(myfilename)
myfilehandle.close()

def sel1():
    try:
        fin1=open('python.txt','a')
        fin2=open('outptNumr.txt','r')
        for line in fin2:
            fin1.write(line)
        fin1.close()
        fin2.close()
    except Exception as e:
        print e
        
def sel2():
    try:
        fin1=open('python.txt','a')
        fin2=open('outptNumber.txt','r')
        for line in fin2:
            fin1.write(line)
        fin1.close()
        fin2.close()
    except Exception as e:
        print e
    myfilehandle=open(myfilename)
    for line in myfilehandle:
        print line
    myfilehandle.close()


fres=open('reccords.txt')
mycoords=[]
for line in fres:
    line1=line.split(',')
    mycoords.append([(line1[0],line1[1]),(line1[2],line1[3].strip())])
fres.close()

def drawSquareWithCoords(mycoords):
    for coord in mycoords:
        x1=int(coord[0][0])
        x2=int(coord[1][0])
        y1=int(coord[0][1])
        y2=int(coord[1][1])
        print x1,y1,x2,y2
        t1.penup()
        t1.setpos(x1,y1)
        t1.pendown()
        for i in range(4):
            t1.fd(x2-x1)
            t1.left(90)
drawSquareWithCoords(mycoords)

def lab13():
    print "error"
    sel1() 
    print "append"
    sel2()
    drawSquareWithCoords(mycoords)


def main():
    lab13()

    
if __name__=="__main__":
    main()

raw_input()
