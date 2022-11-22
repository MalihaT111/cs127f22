#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 23, 2022
#This program does stuff

print("(a) convert centimeters to feet")
print("(b) convert centimeters to feet and inches")
print("(c) convert feet and inches to centimeters")

entry = input("Enter a or b or c: ")
if entry == 'a':
    cm = int(input("Enter height in centimeters:"))
    ft = round(cm/30.48,2)
    print("height is "+ str(ft)+ " feet")
    #convert cm to feet 
if entry == 'b':
    cm = int(input("Enter height in centimeters:"))
    ft = int(cm/30.48)
    inch = int((cm - ft * 30.48) / 2.54)
    if inch == 0:
        print("height is "+ str(ft)+ " feet")
    else:
        print("height is "+ str(ft)+ " feet and "+str(inch)+" inches")
    #convert cm to feet and inches
if entry == 'c':
    fts,inches = (input("Enter height in feet and inches, separated by a space: ").split())
    ft = int(fts)
    inch = int(inches)
    cm = (ft*30.48) + (2.54*inch)
    print("height is " + str(round(cm,0))+ (" centimeters"))
    #convert feet and inches to centimeters

else:
    print("Wrong choice, please enter only a or b or c.")