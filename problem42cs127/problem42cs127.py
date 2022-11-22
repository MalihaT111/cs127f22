#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 15, 2022
#This program does stuff
import folium
import pandas as pd
outname = input("Enter output file: ")
hospital = pd.read_csv("nyc_hospitals.csv")
mapHos = folium.Map()
for index, row in hospital.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Facility Name"]
    newMarker = folium.Marker([lat,lon],popup=name)
    newMarker.add_to(mapHos)
mapHos.save(outname)