from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_points = 0
        self.r_points = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_points, align="center", font=("Courier", 80, "normal"))  # Update to l_points
        self.goto(100, 200)
        self.write(self.r_points, align="center", font=("Courier", 80, "normal"))  # Update to r_points

    def l_score(self):
        self.l_points += 1
        self.update_scoreboard()

    def r_score(self):
        self.r_points += 1
        self.update_scoreboard()
