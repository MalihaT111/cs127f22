#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 15, 2022
#This program does stuff
import numpy as np
import matplotlib.pyplot as plt
print("Enter 1 to get upper right corner\nEnter 2 to get middle portion")
enter = input("Your choice: ")
if enter == '1':
    infile = input("Enter input file name: ")
    outfile = input("Enter output file name: ")
    img = plt.imread(infile)
    height = img.shape[0]
    width = img.shape[1]
    img2 = img[0:height//2:,width//2:width]
    plt.imsave(outfile,img2)
    #plt.imshow(img2)
    #plt.show()
    #get upper right corner of image
if enter == '2' :
    infile = input("Enter input file name: ")
    outfile = input("Enter output file name: ")
    img = plt.imread(infile)
    height = img.shape[0]
    width = img.shape[1]
    img3 = img[(height//4):(height*3)//4:,width//4:(width*3)//4]
    plt.imsave(outfile,img3)
    #plt.imshow(img2)
    #plt.show()
    #get middle portion 
if enter != '1' and enter != '2' :
    print("wrong choice")