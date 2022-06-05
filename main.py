# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh


from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep


# Seting up the Screen
s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong Game")
s.tracer(0)


# Setting up the Paddle & Ball
paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))
ball = Ball()


# Setting up the Controls
s.listen()
s.onkey(paddle1.go_up, "w") 
s.onkey(paddle1.go_down, "s") 
s.onkey(paddle2.go_up, "Up")
s.onkey(paddle2.go_down, "Down")


# Main Game Loop
game_on = True
while game_on:
    sleep(0.1)
    s.update()
    ball.move()


s.exitonclick()