#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 15, 2022
#This program does stuff
import turtle
#t = turtle.Turtle
def flowerRecursion(t,n):
    if n > 0 :
        t.forward(100)
        t.left(105)
        t.forward(52)
        t.left(105)
        t.forward(100)
        t.right(170)
        flowerRecursion(t,n-1)
#flowerRecursion(turtle.Turtle(), 9)
    