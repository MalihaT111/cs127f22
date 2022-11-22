#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 14, 2022
#This program does stuff
import pandas as pd
import matplotlib.pyplot as plt
output = input("Enter name of output file: ")

pop = pd.read_csv('country_internet (1).csv')
# internet users over the population of every country, 
pop['Percentage']=(pop['Internet users']/pop['Population'])*100
pop.plot(x='Country',y='Percentage')
'''groupedData = pop.groupby('Country')
print(groupedData.get_group("136")['Percentage'])'''
#plt.show()

plt.savefig(output)





