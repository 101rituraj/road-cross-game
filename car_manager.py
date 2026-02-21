from turtle import Turtle
import random

CAR_STARTING_POSITION = (400, 0)
CAR_STARTING_X_POSITION = 400
CAR_STARTING_Y_POSITION = []
for x in range(-250 , 251 , 20):
    CAR_STARTING_Y_POSITION.append(x)

car_colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_steps = 5

    def random_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.setheading(180)
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(x=CAR_STARTING_X_POSITION, y=random.choice(CAR_STARTING_Y_POSITION))
            new_car.color(random.choice(car_colors))
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.car_steps)