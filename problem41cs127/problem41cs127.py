#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 15, 2022
#This program does stuff
import folium
#Create a map, centered (0,0), and zoomed out a bit:
mapWorld = folium.Map(location=[40.75, -74.125])
folium.Marker(location = [40.7812, -73.9665],popup="Central Park").add_to(mapWorld)
#Save the map:
mapWorld.save(outfile='nyc_Central_Park.html')