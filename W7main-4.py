import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.pencolor("RED")
t1.shape("turtle")


def saveTracks():
    t1.penup()
    mytrack=list()

    t1.goto(-400,300)
    t1.pendown()

    mytrack.append(t1.pos())

    t1.left(90)
    t1.left(90)
    t1.left(90)
    t1.forward(80)
    t1.forward(20)
    t1.forward(20)

    mytrack.append(t1.pos())


    t1.left(90)
    t1.forward(100)
    t1.forward(100)
    t1.forward(100)

    mytrack.append(t1.pos())

    t1.left(90)
    t1.left(90)
    t1.left(90)
    t1.forward(100)
    t1.forward(100)
    t1.forward(20)
    t1.forward(20)
    t1.forward(20)

    mytrack.append(t1.pos())

    t1.left(90)
    t1.forward(100)
    t1.forward(100)
    t1.forward(20)

    mytrack.append(t1.pos())

    t1.left(90)
    t1.left(180)

    t1.forward(100)

    mytrack.append(t1.pos())


    t1.left(90)
    t1.forward(100)
    t1.forward(100)

    mytrack.append(t1.pos())


def replayTracks(mytrack):
    for t in mytrack:
        print t

def lap7():
    mytrack=saveTracks()
    replayTracks(mytrack)

def main():
    lap7()

if __name__=="__main__":
    main()

main()
raw_input('ㅎㅎ')

wn.exitonclick()
