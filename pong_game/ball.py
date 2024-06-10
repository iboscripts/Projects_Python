from turtle import Turtle


class Ball:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape("circle")
        self.turtle.color("white")
        self.turtle.shapesize(stretch_wid=1, stretch_len=1)
        self.turtle.penup()
        self.turtle.x_move = 10
        self.turtle.y_move = 10
        self.speed = 1

    def move(self):
        new_x = self.turtle.xcor() + self.turtle.x_move
        new_y = self.turtle.ycor() + self.turtle.y_move
        self.turtle.goto(new_x, new_y)

    def bounce_y(self):
        self.turtle.y_move *= -1
        self.increase_speed()

    def bounce_x(self):
        self.turtle.x_move *= -1
        self.increase_speed()

    def increase_speed(self):
        self.turtle.x_move += self.speed
        self.turtle.y_move += self.speed

    def reset_position_r(self):
        self.turtle.goto(0 ,0)
        self.bounce_x()

    def reset_position_l(self):
        self.turtle.goto(0, 0)
        self.bounce_x()

