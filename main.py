"""imported Turtle and Screen class from the turtle module"""
from turtle import Turtle, Screen

"""imported Snake class from snake module"""
from snake import Snake

"""imported time module"""
import time

"""created an object using the screen class"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    # turning off the tracer

"""creating the snake object"""
snake = Snake()

isGameOn = True

while isGameOn:
    screen.update()
    """created delay in animation"""
    time.sleep(0.1)

    snake.moveSnake()

"""screen will exit on click"""
screen.exitonclick()
