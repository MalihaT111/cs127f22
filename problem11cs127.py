##Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 17, 2022
#This program does stuff

import turtle				

turtle.colormode(255)		
t = turtle.Turtle()		

for i in range (2) :
    t.pendown()
    for j in range(0,255,10):	
        t.pensize(j)		
        t.color(0,j,j)
        t.forward(10)
    t.penup()
    t.backward(255)
    t.left(90)
t.right(90)