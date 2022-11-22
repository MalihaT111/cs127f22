#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 17, 2022
#This program prints out letters, unicode, and the next two letters.
phrase = input("Enter a phrase: ")
print ("letter ASCII text_two_letter")
for i in range (len(phrase)):
    x = phrase[i]
    print("%6c %5i %15c"%(x,ord(x),chr(ord(x)+2)))
