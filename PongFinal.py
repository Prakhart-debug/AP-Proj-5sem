import turtle
import time

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)  #prevents window from updating..helps run game smoother


#score
scoreA = 0
scoreB= 0

#paddle A

paddleA=turtle.Turtle()
paddleA.speed(0) #speed of animation
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)

#paddle B
paddleB=turtle.Turtle()
paddleB.speed(0) #speed of animation
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0) #speed of animation
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 4.085 #change when ball moving too fast or slow
ball.dy = -4.085 #change when ball moving too fast or slow

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0   Player B : 0",align="center",font=("Courier",24,"normal"))


#Function
def paddleA_Up():
    y = paddleA.ycor()
    y += 30
    paddleA.sety(y)

def paddleA_Down():
    y = paddleA.ycor()
    y -= 30
    paddleA.sety(y)

def paddleB_Up():
    y = paddleB.ycor()
    y += 30
    paddleB.sety(y)

def paddleB_Down():
    y = paddleB.ycor()
    y -= 30
    paddleB.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(paddleA_Up,"w")
wn.onkeypress(paddleA_Down,"s")

wn.onkeypress(paddleB_Up,"Up")
wn.onkeypress(paddleB_Down,"Down")


#main game

while True:
    time.sleep(1/60) #keep frame rate constant
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A : {}   Player B : {}".format(scoreA,scoreB), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A : {}   Player B : {}".format(scoreA, scoreB), align="center",font=("Courier", 24, "normal"))

    # paddle and ball collisions
    if (ball.xcor() >340 and ball.xcor()<350)and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1.05

    if (ball.xcor() <-340 and ball.xcor()>-350)and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1.05




