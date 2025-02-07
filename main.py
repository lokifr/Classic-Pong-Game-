import time
import turtle
from turtle import Screen, write
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Setup screen
sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor('black')
sc.title("Pong")
sc.tracer(0)

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

# Move paddles
def r_paddle_up():
    r_paddle.go_up()

def r_paddle_down():
    r_paddle.go_down()

def l_paddle_up():
    l_paddle.go_up()

def l_paddle_down():
    l_paddle.go_down()



sc.listen()
sc.onkeypress(r_paddle_up, "Up")
sc.onkeypress(r_paddle_down, "Down")
sc.onkeypress(l_paddle_up, "w")
sc.onkeypress(l_paddle_down, "s")

# Main game loop
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()

    # Collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Right paddle miss
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_pos()

    # Left paddle miss
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_pos()

sc.exitonclick()
