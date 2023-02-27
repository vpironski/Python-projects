import turtle

wn = turtle.Screen()
wn.title("Ping-Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

color = str(input('Enter color (player 1): '))
color2 = str(input('Enter color (player 2): '))

# резултат - променливи
score_a = 0
score_b = 0

# Хилка А
paddle_a = turtle.Turtle()
paddle_a.speed(4)
paddle_a.shape("square")
paddle_a.color(color)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Хилка B
paddle_b = turtle.Turtle()
paddle_b.speed(4)
paddle_b.shape("square")
paddle_b.color(color2)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# топче
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0
ball.speed = 10

# резултат
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player ONE: 0  Player TWO: 0", align="center", font=("Courier", 24, "normal"))

# Движения на хилката
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)

# копчета
wn.listen()
wn.onkeypress(paddle_a_up,"W")
wn.onkeypress(paddle_a_down,"S")
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main loop
while True:
    wn.update()

    # движението на топчето
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # ---граници--- 

    # горна и долна стена
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #os.system("afplay bounce.wav&")

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #os.system("afplay bounce.wav&")

    # лява и дясна стена
    if ball.xcor() > 370:
        score_a += 1
        pen.clear()
        pen.write("Player ONE: {}  Player TWO: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)
        ball.dy = 0
        ball.dx *= -1

    elif ball.xcor() < -370:
        score_b += 1
        pen.clear()
        pen.write("Player ONE: {}  Player TWO: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)
        ball.dy = 0
        ball.dx *= -1

    # сблъсък на хилките и топчето 
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        if ball.dy == 0:
            ball.dy = 0.1

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        if ball.dy == 0:
            ball.dy = 0.1 