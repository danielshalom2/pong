import turtle
import winsound
from paddle import Paddle
from ball import Ball
from pen import Pen
#import os


def main():
    wn = turtle.Screen()
    wn.title("Pong Game")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    paddle_a = Paddle((-350,0),'blue','square')
    paddle_b = Paddle((350,0),'red','square')
    ball = Ball()
    pen = Pen()

        

    # Keyboard binding
    wn.listen()
    wn.onkeypress(paddle_a.paddle_up,"w")
    wn.onkeypress(paddle_b.paddle_up,"Up")
    wn.onkeypress(paddle_a.paddle_down,"s")
    wn.onkeypress(paddle_b.paddle_down,"Down")
        

    while True:
        wn.update()
        
        #move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        #border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        
        if ball.xcor() > 390:
            ball.goto(0 , 0)
            ball.dx *= -1
            pen.score_a += 1
            pen.clear()
            pen.write("Player 1: {} Player 2: {}".format(pen.score_a, pen.score_b),align="center", font=("Courier",24,"normal"))  
        
        if ball.xcor() < -390:
            ball.goto(0 , 0)
            ball.dx *= -1 
            pen.score_b += 1
            pen.clear()
            pen.write("Player 1: {} Player 2: {}".format(pen.score_a, pen.score_b),align="center", font=("Courier",24,"normal")) 
                    
        #paddle & ball collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
            ball.setx(340)
            ball.dx *= -1
            #os.system("aplay pong.wav&") for linux
            winsound.PlaySound("pong.wav", winsound.SND_ASYNC)
        
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
            ball.setx(-340)
            ball.dx *= -1
            #os.system("aplay pong.wav&") for linux
            winsound.PlaySound("pong.wav", winsound.SND_ASYNC)


if __name__ == '__main__':
    main()