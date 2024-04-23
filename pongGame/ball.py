from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.move_speed = 0.1
        self.x_pos = 10
        self.y_pos = 10

    def refresh(self):
        new_x = self.xcor() + self.x_pos
        new_y = self.ycor() + self.y_pos
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_pos *= -1

    def bounce_x(self):
        self.x_pos *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_pos *= -1