from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.move_up_key = None
        self.move_down_key = None
        self.is_moving_up = False
        self.is_moving_down = False

    def set_keys(self, move_up_key, move_down_key, screen):
        """Задає клавіші для керування ракеткою."""
        self.move_up_key = move_up_key
        self.move_down_key = move_down_key

        screen.onkeypress(self.start_move_up, move_up_key)
        screen.onkeyrelease(self.stop_move_up, move_up_key)
        screen.onkeypress(self.start_move_down, move_down_key)
        screen.onkeyrelease(self.stop_move_down, move_down_key)

    def start_move_up(self):
        self.is_moving_up = True

    def stop_move_up(self):
        self.is_moving_up = False

    def start_move_down(self):
        self.is_moving_down = True

    def stop_move_down(self):
        self.is_moving_down = False

    def move(self):
        """Рухає ракетку вгору або вниз, якщо клавіша затиснута."""
        if self.is_moving_up:
            self.sety(self.ycor() + 10)
        if self.is_moving_down:
            self.sety(self.ycor() - 10)
