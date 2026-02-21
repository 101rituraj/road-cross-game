from turtle import Turtle

PLAYER_STARTING_POSITION = (0 , -290)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(PLAYER_STARTING_POSITION)

    def move_forward(self):
        self.forward(10)

    def back_at_same_position(self):
        self.goto(PLAYER_STARTING_POSITION)


