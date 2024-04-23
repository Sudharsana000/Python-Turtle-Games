import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Pick a color :- ")
colors = ["violet", "blue", "green", "yellow", "orange", "red"]
tim = []
yaxis = 120
for i in range(len(colors)):
    tim.append(Turtle(shape="turtle"))
    tim[i].color(colors[i])
    tim[i].penup()
    tim[i].goto(x=-230, y=yaxis)
    yaxis -= 40

if user_bet:
    is_race_on = True

while is_race_on:
    for tim_item in tim:
        rand_distance = random.randint(0,10)
        tim_item.forward(rand_distance)
        if tim_item.xcor() >= 250:
            if user_bet == tim_item.pencolor():
                print("You win!")
            else:
                print(f"You lose. The Winner is {tim_item.pencolor()}")
            is_race_on = False
            break

screen.exitonclick()