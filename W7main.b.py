import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


def drawSquareFrom(tracks):
    t1.penup()
    t1.home()
    t1.pendown()
    tracks=dict()
    tracks=({0:(0,0),1:(50,0),2:(50,50),3:(0,50),4:(0,0)})
    
    for i in range(1,5):
        t1.goto(tracks[i])
    for i in range(1,5):
        print tracks[i]
    
def lap7b():
    drawSquareFrom(tracks)    

def main():
    iap7b()

if __name__=="__main__":
    main()

wn=raw_input()

