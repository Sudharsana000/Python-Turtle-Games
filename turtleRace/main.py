from turtle import Turtle, Screen
tim = Turtle()

def mov_forward():
    tim.forward(10)

def mov_backward():
    tim.backward(10)

def mov_right():
    heading = tim.heading() - 10
    tim.setheading(heading)
def mov_left():
    heading = tim.heading() + 10
    tim.setheading(heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()

screen.onkey(key="w", fun= mov_forward)
screen.onkey(key="e", fun= mov_backward)
screen.onkey(key="r", fun= mov_right)
screen.onkey(key="l", fun= mov_left)
screen.onkey(key="c", fun= clear)

screen.exitonclick()