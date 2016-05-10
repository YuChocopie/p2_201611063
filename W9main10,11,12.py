def Coffee():
    allData=list()
    allData=[ ["Coffee","Weter","Milk","Icecream"],
    ["Espresso","No","No","No"],
    ["Long Black","Yes","No","No"],
    ["Flat white","No","Yes","No"],
    ["Cappuccino","NO","Yes - Frothy","No"],
    ["Affogato",'No','No','Yes']]
    data= allData[1:]
    a=0
    for i in data:
        if i[2]=="No":
            a=a
        else :
            a=a+1
    #a의 값은 yes 의 개수#
    print 'milk persent'
    resurt=(100*a/len(data))
    print resurt, "%"



def EnglishMath():
    marks=list()
    marks=[
        ['English', 100],
        ['Math', 200],
        ['English', 200],
        ['Math', 200],
        ['English', 100],
        ['Math', 300]
    ]
    a=0
    d=0
    m=0
    e=0
    for i in range(len(marks)):
        if marks[i][0]=="English":
            e=e+1
        else :
            e=e
    for i in range(len(marks)):
        if not i%2:
            d=d+marks[i][1]
        else:
            m=m+marks[i][1]
    resurt1=(d/e)
    resurt2=(m/(len(marks)-e))
    print 'English'
    print resurt1
    print 'Math'
    print resurt2





def LetItBe():
    lyrics=list()
    lyrics=[
    'When I find myself in times of trouble',
    'Mother Mary comes to me',
    'Speaking words of wisdom let it be',
    'And in my hour of darkness',
    'She is standing right in front of me',
    'Speaking words of wisdom let it be',
    'Let it be let it be',
    'Let it be let it be',
    'Whisper words of wisdom let it be',
    'when the broken-hearted people',
    'Living in the world agree',
    'will be an answer let it be',
    'For though they may be parted',
    'There is still a chance that they will see',
    'There will be an answer let it be',
    'Let it be let it be',
    'Let it be let it be',
    'Yeah there will be an answer let it be',
    'Let it be let it be',
    'Let it be let it be',
    'Whisper words of wisdom let it be',
    'Let it be let it be',
    'Ah let it be yeah let it be',
    'Whisper words of wisdom let it be',
    'And when the night is cloudy',
    'There is still a light that shines on me',
    'Shine on until tomorrow let it be',
    'I wake up to the sound of music',
    'Mother Mary comes to me',
    'Speaking words of wisdom let it be',
    'Let it be let it be',
    'Let it be yeah let it be',
    'Oh there will be an answer let it be',
    'Let it be let it be',
    'Let it be yeah let it be',
    'Whisper words of wisdom let it be',
    ]
    doc=lyrics
    d=dict()
    for line in doc:
        words=line.split()
        for c in words:
            if c not in d:
                d[c]=1
            else :
                d[c]=d[c]+1

    print d
    for v in range(len(d)):
        if d.values()[v]>=20:
            print d.keys()[v], d.values()[v]





def lap9():
    Coffee()
    EnglishMath()
    LetItBe()

def main():
    lap9()

if __name__=="__main__":
    main()

wn=raw_input()
