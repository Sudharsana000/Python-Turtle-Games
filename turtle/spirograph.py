from turtle import Turtle, Screen
import random

tim = Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple = (r, g, b)
    return tuple


tim.color(random_color())
tim.circle(50)

screen = Screen()
screen.exitonclick()
