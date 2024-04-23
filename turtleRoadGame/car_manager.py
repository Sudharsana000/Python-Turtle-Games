import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed_up = STARTING_MOVE_DISTANCE

    def create_car(self):
        flag = random.randint(1,6)
        if flag == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.speed_up)

    def level_up(self):
        self.speed_up += MOVE_INCREMENT


    