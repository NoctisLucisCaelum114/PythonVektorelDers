from turtle import *
import random as r
color("red")
speed(10)
goto(r.randint(-100,100),r.randint(-150,100))
pendown()
for b in range (4):
    color("blue")
    forward(100)
    right(100)