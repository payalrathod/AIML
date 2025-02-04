import turtle
import time
import random

delay = 0.1
score = 0
highscore = 0
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor()
wn.setup(width=600, height=600)
wn.tracer(0)
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "Stop"
food = turtle.Turtle()
colors = random.choice(['red','green','black'])
shapes = random.choice(['square','triangle','circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score: 0 High Score: 0", align="center", font=("candara",24,"bold"))
def group():
    if head.direction != "down"
        head.direction = "up"
def godown():
    if head.direction != "up"
        head.direction = "down"
def goleft():
    if head.direction != "right"
        head.direction = "left"
def goright():
    if head.direction != "left"
        head.direction = "right"
def move():
    if head.direction == "up"
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "down"
        y=head.ycor()
        head.sety(y-20)
    if head.direction == "left"
        y=head.xcor()
        head.sety(x-20)
    if head.direction == "up"
        y=head.xcor()
        head.sety(x+20)
wn.listen()
wn.onkeypress(group,"w")
wn.onkeypress(godown,"s")
wn.onkeypress(goleft,"a")
wn.onkeypress(goright,"d")




# import random
#
# num = random.randint(1,15)
# guess = None
#
# while guess != num:
#     guess = input("enter number: ")
#     guess = int(guess)
#
#     if guess == num:
#         print("correct guess")
#         break
#     else:
#         print("Try again!")