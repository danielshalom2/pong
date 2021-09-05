import turtle


class Paddle(turtle.Turtle):
    
    def __init__(self, position, color, shape):
        super().__init__(shape=shape, visible=False)
        self.penup()
        self.goto(position)
        self.color(color)
        self.shape(shape)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed(0)
        self.showturtle()
    
    def paddle_up(self):
        y = self.ycor()
        if(y < 240):
            y += 20
        self.sety(y)
    
    def paddle_down(self):
        y = self.ycor()
        if(y > -240):
            y -= 20
        self.sety(y)