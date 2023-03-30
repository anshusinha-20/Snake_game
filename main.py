"""imported Turtle and Screen class from the turtle module"""
from turtle import Turtle, Screen

"""imported time module"""
import time

"""created an object using the screen class"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    # turning off the tracer

"""creating the snake body"""
startingPositions = [(0, 0), (-20, 0), (-40, 0)]

bodies = []

for position in startingPositions:
    newBody = Turtle()
    newBody.shape("square")
    newBody.color("white")
    newBody.penup()
    newBody.goto(position)
    bodies.append(newBody)

isGameOn = True

while isGameOn:
    screen.update()
    """created delay in animation"""
    time.sleep(0.1)
    for body in range(len(bodies) - 1, 0, -1):
        newX = bodies[body - 1].xcor()
        newY = bodies[body - 1].ycor()
        bodies[body].goto(newX, newY)
    bodies[0].forward(10)

"""screen will exit on click"""
screen.exitonclick()
