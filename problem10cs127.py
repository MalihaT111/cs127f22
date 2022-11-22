#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 17, 2022
#This program does stuff

p = input("input: ")

storage1 = ""
storage2 = ""
storage3 = ""
for i in (range (len(p),0,-1)):  
    #lower case  
    storage1+= p[i-1]

    #upper case
    storage2+= p[i-1].upper()

    #abbreviation
x = p.split()
for i in x : 
        storage3+= (i[0].upper())

print("user reverse: " + storage1)
print("user reverse upper: " + storage2)
print("user abbreviation: " + storage3)