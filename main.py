import turtle
import time
import random

wn = turtle.Screen()
wn.title('Pong game')
wn.bgcolor('black')
wn.setup(width=800, height= 600)
wn.tracer(0)

# First player
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape('square')
player_a.color('pink')
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-350, 0)

# Second player
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape('square')
player_b.color('white')
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# player speed
speed = 40

# Score
score_a = 0
score_b = 0
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'Player A: {score_a} PlayerB: {score_b}', align='Center', font=('Courier', 24, 'normal'))

# powerup 1

pup1 = turtle.Turtle()
pup1.speed(0)
pup1.shape('circle')
pup1.color('yellow')
pup1.shapesize(stretch_wid=2, stretch_len=2)
pup1.penup()
pup1.goto(0, -200)
# functions

dif_color = ['red', 'green', 'blue', 'pink', 'black', 'white']
def player_a_up():
    y = player_a.ycor()  # takes the paddle current location
    y += speed  # adds 20 pixels to the paddle y cord, so it moves towards up
    player_a.sety(y) # sets the new paddle y cord.


def player_a_down():
    y = player_a.ycor()  # takes the paddle current location
    y -= speed  # removes 20 pixels from current y cord
    player_a.sety(y)  # sets the new y cord


def player_b_up():
    y = player_b.ycor()  # takes the paddle current location
    y += speed  # adds 20 pixels to the paddle y cord, so it moves towards up
    player_b.sety(y) # sets the new paddle y cord.


def player_b_down():
    y = player_b.ycor()  # takes the paddle current location
    y -= speed  # removes 20 pixels from current y cord
    player_b.sety(y)  # sets the new y cord


wn.listen()  # listens what keys you touch
wn.onkeypress(player_a_up, 'w')  # basically if 'w' is pressed, then it activates player_a_up function
wn.onkeypress(player_a_down, "s")
wn.onkeypress(player_b_up, 'o')
wn.onkeypress(player_b_down, 'l')

while True:
    wn.update()

    # ball movement

    # The ball movement at the beginning of the game.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Y CORDS:
    # if ball is about to go out of y frame, it reverses it's movement
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # X Cords
    # if ball goes out of x frame, it goes back to 0,0 cords
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        score_a += 1
        wn.bgcolor(random.choice(dif_color))  # if someone scores, the background color changes

        pen.write(f'Player A: {score_a} PlayerB: {score_b}', align='Center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        wn.bgcolor(random.choice(dif_color))  # if someone scores, the background color changes
        pen.write(f'Player A: {score_a} PlayerB: {score_b}', align='Center', font=('Courier', 24, 'normal'))

    # Paddle and ball collision
    # Right paddle
    if (ball.xcor() > 330 and ball.xcor() < 335) and (ball.ycor() < player_b.ycor() + 50 and ball.ycor() > player_b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
        player_b.color(random.choice(dif_color))

    # Left paddle
    if (ball.xcor() < -330 and ball.xcor() > -335) and (ball.ycor() < player_a.ycor() + 50 and ball.ycor() > player_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        player_a.color(random.choice(dif_color))



    time.sleep(0.005)
