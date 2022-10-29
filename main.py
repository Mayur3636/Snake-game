from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from players import Players
from playsound import playsound
import time

SPEED = 0.3
screen = Screen()

screen.bgcolor("black")
screen.setup(width=600, height=600, startx=300, starty=10)
screen.title("Snake Game")
screen.tracer(0)
name = screen.textinput(title="Player name", prompt="Enter your name")

snake = Snake()
food = Food()
player = Players()

# Screen will listen
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

# Player data added
if not player.is_player_in_data(name):
    player.add_player(name)

player_data = player.get_player(name)
p_name = player_data[0]
p_score = player_data[1]
p_hscore = player_data[2]

score = Scoreboard(p_name, 0, p_hscore)
# playsound('nacho.mp3')
score.write_player_name()
score.write_init_hscore()
screen.update()


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(SPEED)
    snake.move()
    if snake.head.distance(food) <= 18:
        # print("on nom")
        food.refresh()
        snake.extend()
        score.update_score()
        # playsound('beep-07a.wav')

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        score.game_over()

    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            score.game_over()
            is_game_on = False

current_score = score.get_score()
# print(current_score)
player.high_score(player_data, current_score)
h = player.get_high_score(player_data)
# print(h)
score.write_highscore(h)


screen.exitonclick()
