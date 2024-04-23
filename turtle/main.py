import random
from turtle import Turtle, Screen
def move(sides):
    for i in range(sides):
        tim.forward(100)
        tim.right(360/sides)

tim = Turtle()
tim.shape("turtle")

for i in range(3,8):
    move(i)


screen = Screen()
screen.exitonclick()