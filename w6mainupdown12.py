def sumList(aList):
    x=list()
    mysum=0
    for i in range(0,aList):
        if i%4==0 and not i%5==0:
            mysum+=i
    return mysum


def lab6():
    """my homework!!!!"""
    aList=1000
    print sumList(aList)
    
def main():
    lab6()

if __name__=="__main__":
    main()

wn=raw_input()