import turtle
wn=turtle.Screen()
print "Let's start rock scissors paper game"

Player1 = raw_input("P1 : ")
Player2 = raw_input("P2 : ")

S="Scissors"
R="Rock"
P="Paper"

if(Player1==Player2):
    print "Draw"
    
elif(Player1=="S"):
    if(Player2=="P"):
        print 'Scissors Win'
    elif(Player2=="R"):
        print 'Rock Win'
        
elif(Player1=="R"):
    if(Player2=="P"):
        print 'Paper Win'
    elif(Player2=="S"):
        print 'Rock Win'  
        
elif(Player1=="P"):
    if(Player2=="S"):
        print 'Scissors Win'
    elif(Player2=="R"):
        print 'Paper Win' 
else:
    print 'Input Error'

wn.exitonclick()

