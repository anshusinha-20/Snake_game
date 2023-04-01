"""imported Turtle and Screen class from the turtle module"""
from turtle import Turtle, Screen

"""imported Snake class from snake module"""
from snake import Snake

"""imported Food class from the food module"""
from food import Food

"""imported Scoreboard class from the scoreboard module"""
from scoreboard import Scoreboard

"""imported time module"""
import time

"""created an object using the screen class"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)    # turning off the tracer

"""creating the snake object"""
snake = Snake()

"""creating the food object"""
food = Food()

"""creating the score object"""
score = Scoreboard()

"""making up the screen to listen on keystrokes"""
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

isGameOn = True

while isGameOn:
    """screen is updated"""
    screen.update()
    """created delay in animation"""
    time.sleep(0.08)
    """snake object is called and the snake starts moving"""
    snake.moveSnake()

    """if snake eats the food, the food vanishes at the 
    given location and appears at a newer location after collision"""
    if snake.head.distance(food) < 15:
        score.increaseScore()
        food.moveFood()

    """if snake hits the wall, the game is over"""
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        isGameOn = False
        score.gameOver()


"""screen will exit on click"""
screen.exitonclick()
