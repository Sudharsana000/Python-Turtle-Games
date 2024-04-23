from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = -1
        self.update_level()

    def update_level(self):
        self.clear()
        self.hideturtle()
        self.goto(-260, 250)
        self.level += 1
        self.write(f"Level: {self.level}", move=False, font=FONT)

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.level += 1
        self.write(f"Game Over!", move=False, align="center", font=FONT)
