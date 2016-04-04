print "BMI"

height= input("input user height(cm) : ")
weight= input("input user weight(kg) : ")
print (weight,height)
bmi= (weight*10000)/(height*height)

if bmi<18.5:
    print "low weight"
elif bmi >= 18.5 and bmi<25:
    print "normal weight"
elif bmi >= 25 and bmi<30:
    print "overwe weight"
elif bmi >= 30 and bmi<35:
    print "very overwe weight"
else:
    print 'Input Error'