def leapYear():
    year=raw_input("please write year : ")
    year=int(year)
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        print "leap year"
    else :
        print "not leap year"
def lap6():
    leapYear()
def main():
    lap6()
if __name__=="__main__":
    main()