from turtle import Turtle, pos, position


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.score = 0

    def update(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Verdana", 24, "normal"))
