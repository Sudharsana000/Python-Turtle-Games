import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road Crossing Game")
screen.tracer(0)

p = Player()
score = Scoreboard()
car = CarManager()
screen.listen()
screen.onkey(p.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    if p.ycor() >= 300:
        car.level_up()
        score.update_level()
        p.reset()

    for c in car.cars:
        if c.distance(p) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()
