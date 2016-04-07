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
def lab6():
    UpDown()
def main():
    lab6()
if __name__=="__main__":
    main()