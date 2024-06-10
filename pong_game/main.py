from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    if ball.turtle.ycor() > 280 or ball.turtle.ycor() < -280:
        ball.bounce_y()

    if ball.turtle.distance(r_paddle.turtle) < 50 and ball.turtle.xcor() > 320 or ball.turtle.distance(l_paddle.turtle) < 50 and ball.turtle.xcor() < -320:
        ball.bounce_x()

    if ball.turtle.xcor() > 380:
        ball.reset_position_r()
        scoreboard.l_score()

    if ball.turtle.xcor() < -380:
        ball.reset_position_l()
        scoreboard.r_score()

screen.exitonclick()
