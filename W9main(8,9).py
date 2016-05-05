

import math
Locations=(37.571610,126.976677),(37.571641,126.976674),(37.572466,126.990404),(37.570159,126.983013),(37.565909,126.977193)
myList=list()

def nearestsubway():
    for i in Locations:
        distances=math.sqrt((37.575967-i[0])**2 + (126.973619-i[1])**2)
        myList.append(distances)
        print distances
    print "The nearest subway station"
    print min(myList)


import matplotlib
import matplotlib.pyplot as plt

mylist=list()
mylist=[
    [74.425,76.326],
    [61.164 ,61.636],
    [109.688, 115.744],
    [144.796, 146.776],
    [174.996, 181.676],
    [177.841, 177.434],
    [204.630, 205.980],
    [223.373, 232.245],
    [161.055, 166.130],
    [171.576, 176.735],
    [279.169, 293.772],
    [239.450, 251.066],
    [148.690, 156.510],
    [182.977, 196.992],
    [237.792, 242.641],
    [283.869, 296.762],
    [209.344, 210.282],
    [118.965, 114.441],
    [186.503, 186.856],
    [195.734, 203.014],
    [254.381, 249.472],
    [212.401, 229.111],
    [271.654, 295.354],
    [319.197, 335.045],
    [229.829, 231.671]
]
def menAndwoman():
    men=0
    woman=0
    for i in range(0,len(mylist)):
        men=men+mylist[i][0]
        woman=woman+mylist[i][1]
    print "men's sum"
    print men
    print "An average man"
    print men/len(mylist)
    print "woman's sum"
    print woman
    print "An average woman"
    print woman/len(mylist)


    
jongro=(74.425,76.326)
joongo=(61.164 ,61.636)
yungsan=(109.688, 115.744)
sungdong=(144.796, 146.776)
gwangjin=(174.996, 181.676)
dongda=(177.841, 177.434)
joongrang=(204.630, 205.980)
sungbuk=(223.373, 232.245)
gangbuk=(161.055, 166.130)
dobong=(171.576, 176.735)
nowon=(279.169, 293.772)
unpyeng=(239.450, 251.066)
sudamun=(148.690, 156.510)
mapo=(182.977, 196.992)
yangchun=(237.792, 242.641)
gangsu=(283.869, 296.762)
guro=(209.344, 210.282)
gumchun=(118.965, 114.441)
yongdunpo=(186.503, 186.856)
dongjak=(195.734, 203.014)
goanak=(254.381, 249.472)
sucho=(212.401, 229.111)
gangnam=(271.654, 295.354)
songpa=(319.197, 335.045)
gangdong=(229.829, 231.671)

gu={"jongro":jongro,"joongo":joongo,'yungsan':yungsan,'sungdong':sungdong,'gwangjin':gwangjin,'dongda':dongda,'joongrang':joongrang,'sungbuk':sungbuk,'gangbuk':gangbuk,'dobong':dobong,'nowon':nowon,'unpyeng':unpyeng,'unpyeng':unpyeng,'sudamun':sudamun,'mapo':mapo,'yangchun':yangchun,'gangsu':gangsu,'guro':guro,'gumchun':gumchun,'yongdunpo':yongdunpo,'dongjak':dongjak,'goanak':goanak,'sucho':sucho,'gangnam':gangnam,'songpa':songpa,'gangdong':gangdong}

d=dict()

def graph():
    for i in gu:
        d[str(i)]=gu[i][0]+gu[i][1]
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()



def lap9():
    nearestsubway()
    menAndwoman()
    graph()

def main():
    lap9()

if __name__=="__main__":
    main()

wn=raw_input()