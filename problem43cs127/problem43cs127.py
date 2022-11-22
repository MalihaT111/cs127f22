#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 15, 2022
#This program does stuff
import pandas as pd
import folium

file = pd.read_csv("after_school.csv")

print("Enter 1 for Borough/Community,\n2 for Grade Level / Age Group")
choice = input("Your choice: ")

if choice == "1":
    sortedBoroughs = file.groupby("Borough/Community")
    print(sortedBoroughs.groups.keys())

    chosenname = input("Enter Borough/Community name: ")
    choseninfo = sortedBoroughs.get_group(chosenname)

    n2 = chosenname.lower()
    n3 = n2.replace(' ','_')
    n4 = n3.replace('/','_')
    n5 = n4 + "_after_school"
    mapB = folium.Map()
    communityInfo = sortedBoroughs.get_group(chosenname)

    for index, row in communityInfo.iterrows():
        lat = row["Latitude"]
        lon = row["Longitude"]
        n = row["Name"]
        newMarker = folium.Marker([lat,lon],popup=n)
        newMarker.add_to(mapB)
    mapB.save(f"{n5}.html")
if choice == '2':
    sortedG = file.groupby("Grade Level / Age Group")
    print(sortedG.groups.keys())
    chosenG = input("Enter Grade Level / Age Group name: ")
    n2 = chosenG.lower()
    n3 = n2.replace(' ','_')
    n4 = n3.replace('/','_')
    n5 = n4 + "_after_school"
    mapB = folium.Map()
    communityInfo = sortedG.get_group(chosenG)
    for index, row in communityInfo.iterrows():
        lat = row["Latitude"]
        lon = row["Longitude"]
        n = row["Name"]
        newMarker = folium.Marker([lat,lon],popup=n)
        newMarker.add_to(mapB)
    mapB.save(f"{n5}.html")