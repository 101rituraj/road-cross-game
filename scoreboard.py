from turtle import Turtle

LEVEL_POSITION = (-300, 280)
GAME_OVER_POSITION = (0, 0)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(LEVEL_POSITION)
        self.write(f"Level : {self.level}", align="center", font=("Courier", 20, "normal"))

    def level_up(self):
        self.reset()
        self.penup()
        self.hideturtle()
        self.goto(LEVEL_POSITION)
        self.level += 1
        self.write(f"Level : {self.level}", align="center", font=("Courier", 20, "normal"))


    def game_over(self):
        self.goto(GAME_OVER_POSITION)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))