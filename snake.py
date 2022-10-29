from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.eye = Turtle(shape="circle")
        self.eye.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.eye.penup()
        self.eye.color("grey")
        self.eye.goto(STARTING_POS[0])
        self.head = self.snake[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_body_part(pos)

    def add_body_part(self, pos):
        body_part = Turtle("square")
        # body_part.speed("fastest")
        body_part.penup()
        body_part.color("white")
        body_part.goto(pos)
        self.snake.append(body_part)

    def extend(self):
        self.add_body_part(self.snake[-1].position())

    def move(self):
        for j in range(len(self.snake) - 1, 0, -1):
            t = self.snake[j - 1].position()
            self.snake[j].goto(t)
            j -= 1
        self.eye.forward(STEP)
        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.eye.setheading(UP)
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.eye.setheading(DOWN)
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.eye.setheading(LEFT)
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.eye.setheading(RIGHT)
            self.head.setheading(RIGHT)

