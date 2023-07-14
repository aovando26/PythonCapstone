import turtle

wn = turtle.Screen()
wn.title("Pong by Anthony Ovando")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer()

# scores
score_a = 0
score_b = 0
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(4)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 PlayerB: 0", align="center", font=("Verdana", 24, "normal"))
# function for positive y
def paddle_a_up():
    # return the y - coordinate
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


# function for - y-axis
def paddle_a_down():
    # return the y - coordinate
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# function for positive y
def paddle_b_up():
    # return the y - coordinate
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


# function for - y-axis
def paddle_b_down():
    # return the y - coordinate
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, " Up")
wn.onkeypress(paddle_b_down, "Down")


while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} PlayerB: {score_b}", align="center", font=("Verdana", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} PlayerB: {score_b}", align="center", font=("Verdana", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
