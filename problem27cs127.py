#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 6, 2022
#This program does stuff

import matplotlib.pyplot as plt
import pandas as pd

file = input("Enter a csv file: ")
b = input("Enter borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")
o = input("Enter output name: ")

pop = pd.read_csv(file)

print("Min: " + str(pop[b].min()))
print("Max: "+ str(pop[b].max()))
print("Mean: " + str(round(pop[b].mean(),3)))
print("Median: "+ str(pop[b].median()))
print("Standard Deviation: "+str(round(pop[b].std(),3)))
#   covid_daily_cases.csv
pop['Fraction'] = pop[b]/pop['case_count']

#Create a plot of year versus fraction of pop. in Bronx (with labels):

pop.plot(x = 'date_of_interest', y = 'Fraction')
#plt.show()
#plt.imshow(o)
#Save to the file:  fractionBX.png
plt.savefig(o)
