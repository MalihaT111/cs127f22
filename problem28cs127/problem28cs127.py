#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 14, 2022
#This program does stuffimport matplotlib.pyplot as plt
import pandas as pd
i = input("Enter a choice:\na. group by borough\nb. group by year\n")

file = pd.read_csv('children_lead.csv')
if i == 'a':
    print("average number of affected children by borough")
    groupb = file.groupby("borough")
    print(groupb['affected_children'].mean())
    b = input("Enter a borough: ")
    bro = file.groupby("borough").get_group(b)
    print("average number of affected children of " + b + "is " + str(bro['affected_children'].mean()) )
    print("min number of affected children of " + b + " is " + str(bro['affected_children'].min()) )
    print("max number of affected children of " + b + " is " + str(bro['affected_children'].max()) )
if i == 'b':
    print("average number of affected children by year")
    groupy = file.groupby("year")
    print(groupy['affected_children'].mean())
    y = input("Enter a year (2005 - 2016): ")
    yro = file.groupby("year").get_group(int(y))
    print("average number of affected children in " + y + " is " + str(yro['affected_children'].mean()) )
    print("min number of affected children in "+y+" is "+str(yro['affected_children'].min()))
    print("max number of affected children in "+y+" is "+str(yro['affected_children'].max()))
if i != 'a' and i != 'b':
    print("wrong choice")
