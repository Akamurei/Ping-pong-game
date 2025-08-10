from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
left_paddle.set_keys("w", "s", screen)
right_paddle.set_keys("Up", "Down", screen)
screen.listen()

def game_loop():
    global scoreboard
    ball.move()
    left_paddle.move()
    right_paddle.move()
    screen.update()
    screen.ontimer(game_loop, 20)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 390:
        scoreboard.l_ball_win()
        ball.reset_ball()


    if ball.xcor() < -390:
        scoreboard.r_ball_win()
        ball.reset_ball()
    if scoreboard.winner():
        ball.winner_ball()

game_loop()
screen.mainloop()
