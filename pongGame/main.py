import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.refresh()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if paddle1.distance(ball) < 50 and ball.xcor() > 320 or paddle2.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.update2()

    if ball.xcor() < -420:
        ball.reset_position()
        scoreboard.update1()

screen.exitonclick()