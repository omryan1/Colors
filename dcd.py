#Initialize Turtle
import turtle
import random
t = turtle.Turtle()
t.left(90)

#Functions
def randomDot():
    t.color("Blue")
    t.begin_fill()
    t.circle(49)
    t.end_fill()
    
#Main
randomDot()
