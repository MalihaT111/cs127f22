#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 23, 2022
#This program does stuff
import numpy as np
from matplotlib import pyplot as plt

size = input("Enter the size: ")
outputname = input("Enter output file: ")
image = np.empty([int(size),int(size),3])
# if, else <333
for i in range (int(size)):
    if i%2 == 0:  #green   
        image[:,i,0] = 0 #r
        image[:,i,1] = 0 #g
        image[:,i,2] = 1.0 #b
    else:  #blue actuallyswitch lolol 
        image[:,i,0] = 0
        image[:,i,1] = 1.0
        image[:,i,2] = 0

#plt.imshow(image)
#plt.show()

plt.imsave(outputname,image)