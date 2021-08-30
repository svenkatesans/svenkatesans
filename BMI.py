weight = int(input("Enter  your weight in KG : "))

lenght  = int(input("Enter  your lenght  in cm  : "))


dittname = str(input("Enter  your namn in  : "))

dittname = dittname.upper()


bmi = weight/((lenght/100)**2)
print(' New  BMI --' + str(dittname) + ' with the vikt ' + str(weight) + " and the BMI is " + str(bmi))
if bmi <=  18.5:
    print ("du är undervikt")
elif bmi <=18.5 and bmi <= 24.9:
    print ("du är normalvikt")
elif bmi >= 25 and bmi <= 29.9:
    print ("du är övervikt")
elif bmi <= 30:
    print ("du är fetma")


