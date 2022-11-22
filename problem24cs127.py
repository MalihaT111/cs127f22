#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 26, 2022
#This program does stuff, hw24
#apple banana cantalope durian shrub
#af bce gdfgb agcg edc dade fggga gb
list1 = input("Enter a list of words, separated by a space: ")
list2= list1.split(' ')
print("number of words: ",(len(list2)))
lettera = "a"
letterb = "b"
number = 0
for i in range (len(list2)):
    if lettera in list2[i][-1]:
        number += 1
    if letterb in list2[i][-1]:
        number +=1
fraction = round(number/len(list2),2)
print("number of words ending with a or b: ", number)
print("fraction of words ending with a or b: ", fraction)
