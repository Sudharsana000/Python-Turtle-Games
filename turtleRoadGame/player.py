from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.tilt(90)
        self.reset()

    def reset(self):
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        y = self.ycor() + 10
        self.goto(self.xcor(), y)