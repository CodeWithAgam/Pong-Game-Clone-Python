from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def move(self):
        x = self.xcor() + 10 
        y = self.ycor() + 10 
        self.goto(x, y)

    def bounce(self):
        if self.ycor() > 290:
            self.setheading(self.heading() + 20)
            self.setx(200)

        # if self.ycor() < -290:
        #     self.setxy(-290)
        #     self.sety(-290)