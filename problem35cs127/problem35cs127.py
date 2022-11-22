#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 15, 2022
#This program does stuff
enter = int(input("Enter hour (in 24 hour time): "))
if enter < 12:
    print("Good morning")
if enter >= 12 and enter < 17:
    print("Good afternoon")
if enter >=17 and enter <=24:
    print("Good evening")