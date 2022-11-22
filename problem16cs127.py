##Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 17, 2022
#This program does stuff
names = input("Enter a list of names, separated by semicolon: ")
s = names.split(';')
for i in range(len(s)):
    s[i] = s[i].split()
for i in s :
    print((i[0])[0:1]+". "+i[1])

    

