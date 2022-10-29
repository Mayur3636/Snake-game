from turtle import Turtle
import random
MAX_WIDTH = int(560/2)
MAX_HEIGHT = int(560/2)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        y = random.randint(-MAX_HEIGHT, MAX_HEIGHT)
        x = random.randint(-MAX_WIDTH, MAX_WIDTH)
        p = (x, y)
        while x != int(self.xcor()) and y != int(self.ycor()):
            y = random.randint(-MAX_HEIGHT, MAX_HEIGHT)
            x = random.randint(-MAX_WIDTH, MAX_WIDTH)
            p = (x, y)
        self.goto(p)