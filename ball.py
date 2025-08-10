from turtle import Turtle

SPEED_OF_BALL = 1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 5
        self.y = 5
        self.ball_speed = SPEED_OF_BALL


    def move(self):
        new_x = self.xcor() + (self.x * self.ball_speed)
        new_y = self.ycor() + (self.y * self.ball_speed)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1
    def bounce_x(self):
        self.x *= -1
        self.ball_speed *= 1.1

    def reset_ball(self):
        self.goto(0, 0)
        self.ball_speed = SPEED_OF_BALL
        self.bounce_x()

    def winner_ball(self):
        self.goto(0,60)
        self.ball_speed = 0






