#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 15, 2022
#This program does stuff
import turtle 
def petal (color,angle):
    turtle.colormode(255)
    t = turtle.Turtle(visible = False)
    t.left(angle)
    for i in range(0,255,10):
        t.forward(10)
        t.pensize(i)		
        if color == "red":
            t.pencolor(i,0,0)
        elif color == "blue":
            t.pencolor(0,0,i)
        elif  color == "green":
            t.pencolor(0,i,0)
        elif color == "cyan":
            t.pencolor(0,i,i)
        elif color == "yellow":
            t.pencolor(i,i,0)
        elif color == "pink":
            t.pencolor(i,0,i)
        else:
            t.pencolor(0,i,0)


def flower (color,numpetals) :
    angle = 0 
    for j in range(numpetals):
        petal(color,angle)
        angle+=360/numpetals

def main():
    flower("green",9)





