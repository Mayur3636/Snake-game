from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 15, "bold")

# This will do our task of writing


class Scoreboard(Turtle):

    def __init__(self, player, escore, hscore):
        super().__init__()
        self.name_of_player = player
        self.hideturtle()
        self.color("white")
        self.score = escore
        self.hscore = hscore
        self.write_score()

    def get_score(self):
        s = self.score
        return s

    def write_score(self):
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def write_player_name(self):
        n = self.name_of_player
        new_turt = Turtle()
        new_turt.hideturtle()
        new_turt.color("white")
        new_turt.penup()
        new_turt.goto(-280, 270)
        new_turt.write(f"Hi {n}!", align="left", font=FONT)

    def write_init_hscore(self):
        n = self.name_of_player
        new_turt = Turtle()
        new_turt.hideturtle()
        new_turt.color("white")
        new_turt.penup()
        new_turt.goto(200, 270)
        new_turt.write(f"High score: {self.hscore}", align=ALIGN, font=FONT)

    def write_highscore(self, hscore):
        n = self.name_of_player
        n_turt = Turtle()
        n_turt.hideturtle()
        n_turt.color("white")
        n_turt.penup()
        n_turt.goto(0, 240)
        n_turt.write(f"Yor High score {hscore}", align=ALIGN, font=FONT)






