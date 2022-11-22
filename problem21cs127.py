
##Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 18, 2022
#This program does stuff
import matplotlib.pyplot as plt
import numpy as np

p = input("Enter file name: ")
thresh= float(input("Enter threshold: "))

ca = plt.imread(p)   #Read in image
countSnow = 0            #Number of pixels that are almost white             #Threshold for almost white-- can adjust between 0.0 and 1.0
countPixels = 0
percent = 0
#For every pixel:
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          #Check if red, green, and blue are > t:
          if (ca[i,j,0] > thresh) and (ca[i,j,1] > thresh) and (ca[i,j,2] > thresh):  # r    g   b, greater than , 
            # all is necessary bc white 
               countSnow = countSnow + 1
          if (ca[i,j,0]<=255):
               countPixels+=1
          
percent = ((countSnow/countPixels)*100)
print("number of white pixels: ", countSnow)
print("percent of white pixels: ",percent,"%")