import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.dx = 0.1
        self.dy = 0.1
        self.showturtle()
        