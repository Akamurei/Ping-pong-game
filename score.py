from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left = "Left"
        self.right = "Right"
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.write(f'{self.l_score} | {self.r_score}', align='center', font=('Arial', 20, 'normal'))
        self.WINNING_SCORE = 20

    def l_ball_win(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_ball_win(self):
        self.r_score += 1
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f'{self.l_score} | {self.r_score}', align='center', font=('Arial', 20, 'normal'))



    def winner(self):
        if self.l_score >= self.WINNING_SCORE:
            self.goto(0, 0)
            self.write("🏆 Left Player Wins! 🏆", align="center", font=("Courier", 24, "bold"))
            return True
        elif self.r_score >= self.WINNING_SCORE:
            self.goto(0, 0)
            self.write("🏆 Right Player Wins! 🏆", align="center", font=("Courier", 24, "bold"))
            return True
        return False






