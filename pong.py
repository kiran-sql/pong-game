import turtle

win = turtle.Screen()
win.title("Pong by Kiran")
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0, 0)

# score
score_a = 0
score_b = 0

# paddle A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("black")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-350, 0)


# paddle B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("black")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(350, 0)


# ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1


# score
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
          font=("Courier", 20, "normal"))

# function to move the paddle


def player_a_up():
    y = player_a.ycor()
    y += 20
    player_a.sety(y)


def player_b_up():
    y = player_b.ycor()
    y += 20
    player_b.sety(y)


def player_a_down():
    y = player_a.ycor()
    y -= 20
    player_a.sety(y)


def player_b_down():
    y = player_b.ycor()
    y -= 20
    player_b.sety(y)


# keyboard binding to move the paddle
win.listen()
win.onkeypress(player_a_up, "w")
win.onkeypress(player_b_up, "p")
win.onkeypress(player_a_down, "z")
win.onkeypress(player_b_down, "m")


# main game loop
while True:
    win.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if(ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1
    if(ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1

    if(ball.xcor() > 390):
        ball.goto(0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 20, "normal"))

    if(ball.xcor() < -390):
        ball.goto(0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 20, "normal"))

    if((ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < player_b.ycor() + 50 and ball.ycor() > player_b.ycor()-50):
        ball.setx(340)
        ball.dx *= -1

    if((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_a.ycor() + 50 and ball.ycor() > player_a.ycor()-50)):
        ball.setx(-340)
        ball.dx *= -1
