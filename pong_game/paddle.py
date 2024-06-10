from turtle import Turtle


class Paddle:
    def __init__(self, x, y):
        self.turtle = Turtle()
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.shapesize(stretch_wid=5, stretch_len=1)
        self.turtle.penup()
        self.turtle.goto(x, y)

    def go_up(self):
        new_y = self.turtle.ycor() + 20
        self.turtle.sety(new_y)

    def go_down(self):
        new_y = self.turtle.ycor() - 20
        self.turtle.sety(new_y)


