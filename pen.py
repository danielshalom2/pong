import turtle

class Pen(turtle.Turtle):
    score_a = 0
    score_b = 0
    def __init__(self):
        super().__init__()
        self.speed()
        self.color("white")
        self.penup()
        
        self.goto(0,260)
        self.write("Player 1: {} Player 2: {}".format(self.score_a, self.score_b),align="center", font=("Courier",24,"normal"))
        self.hideturtle() 