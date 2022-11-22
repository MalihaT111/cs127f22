#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 15, 2022
#This program does stuff
import pandas as pd
file = pd.read_csv("movie_locations.csv")
n = input("order of most popular neighborhoods in movies: ")
print(file["Neighborhood"].value_counts()[:int(n)])
d = input("order of directors/filmakers making most movies in NYC: ")
print(file["Director/Filmmaker Name"].value_counts()[:int(d)])