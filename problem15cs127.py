#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 17, 2022
#This program does stuff
p = input("Enter a phrase: ")
phrase = p.split()
for i in range(len(phrase),0,-1):
    print(' '.join(phrase[:i]))
   
for i in range (len(phrase)-1):
    print(' '.join(phrase[:i+2])) 

