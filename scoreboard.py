"""imported Turtle class from the turtle module"""
from turtle import Turtle

"""Constants"""
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

"""Scoreboard class is created"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.score = 0
        self.updateScoreBoard()


    def updateScoreBoard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.clear()
        self.score += 1
        self.updateScoreBoard()






