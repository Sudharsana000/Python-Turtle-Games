from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.high_score = 0
        self.goto((0, 270))
        self.refresh()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", move=False, align='center', font=('Arial', 20, 'normal'))
    #     self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.refresh()