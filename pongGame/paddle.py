from turtle import Turtle

WIDTH = 20
HEIGHT = 100


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)