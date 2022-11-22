##Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 17, 2022
#This program does stuff
import matplotlib.pyplot as plt
import numpy as np

i = input("Enter name of the input file: ")
o = input("Enter name of the output file: ")

img = plt.imread(i)   
plt.imshow(img)		                 #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,0] = 0


plt.imshow(img2)         #Load our new image into pyplot
plt.show()               #Show the image (waits until closed to continue)

plt.imsave('o', img2)  #Save the image we created to the file: reds.png