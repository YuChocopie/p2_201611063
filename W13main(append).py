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
def lab13():
    print "error"
    sel1() 
    print "append"
    sel2()
    
def main():
    lab13()

    
if __name__=="__main__":
    main()

raw_input()
