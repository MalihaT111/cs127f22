#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 14, 2022
#This program does stuff
import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('country_internet.csv')
groupP = file.groupby("Continental region")

print(groupP["NO. OF Internet Plans"].mean())
print("possible regions are")
print(groupP.groups.keys())

region = input("choose a region: ")
print("In region "+region)

bro = groupP.get_group(region)

print("number of countries: "+ str(bro['Country'].nunique()))
print("maximum number of internet plans: "+ str(bro['NO. OF Internet Plans'].max()))
print("minimum number of internet plans: "+ str(bro['NO. OF Internet Plans'].min()))

output = input("Please enter output file name: ")

bro.plot.bar('Country','NO. OF Internet Plans')
plt.gcf().subplots_adjust(bottom=0.25)
plt.xlabel(f'Country in {region}')
plt.ylabel('NO. OF Internet Plans')
#plt.show()
plt.savefig(output)

