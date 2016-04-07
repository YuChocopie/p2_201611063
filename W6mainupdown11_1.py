def leapYear():
    year=raw_input("please write year : ")
    year=int(year)
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        print "leap year"
    else :
        print "not leap year"

"""
%%plantuml
@startuml
start

:This year is leap year??;
if (year is divided by 4 and year is divided by 100 or divided by 400) then (correct)
    :print "YES";
else (non correct)
    :print "NO";
endif
stop

"""
def UpDown():
    man=input("please write number : ")
    chance=input("please write chance : ")
    for i in range(chance):
        woman=input("please write number : ")
        if man>woman :
            print "Up"
        elif man<woman:
            print "Down"
        elif man==woman:
            print "Ding~ Dong~ Dang~"
            break
    print "Game over"
                

"""


@startuml
start

:man : Write your number(=a);
:woman : Choose your playing chance(=x) and write your number(=b);

while( )
if (non a=b) then (a<b)
:Up;
else (a>b)
:Down;
endif
endwhile
:chance is over or a=b;
if ( ) then (over chance)
:End Game;
else (a=b)
:Ding~ Dong~ Dang~;
endif
 
:Game over;

@enduml

"""


def lap6():
    leapYear()
    UpDown()

def main():
    lap6()
if __name__=="__main__":
    main()