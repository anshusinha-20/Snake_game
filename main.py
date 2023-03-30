"""imported Turtle and Screen class from the turtle module"""
from turtle import Turtle, Screen

"""created an object using the screen class"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

"""creating the snake body"""
startingPositions = [(0, 0), (-20, 0), (-40, 0)]

for position in startingPositions:
    newBody = Turtle()
    newBody.shape("square")
    newBody.color("white")
    newBody.goto(position)

"""screen will exit on click"""
screen.exitonclick()
