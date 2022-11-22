##Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 17, 2022
#This program does stuff
import turtle				

turtle.colormode(255)		
t = turtle.Turtle()
#t.backward(255)
for i in range(0,255,10):
        t.pensize(i)		
        t.color(i,0,i)
        t.forward(10)

for j in range(255,0,-10):
        t.pensize(j)		
        t.color(j,0,j)
        t.forward(10)