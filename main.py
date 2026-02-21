from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

LEVEL = 1
screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)

screen.listen()

player = Player()
car = CarManager()
scoreboard = ScoreBoard()

screen.onkey(key="Up", fun=player.move_forward)

game = True
while game:
    time.sleep(0.1)
    screen.update()
    car.random_car()
    car.car_move()

    #detect whether turtle reached finish line or not
    if player.ycor() > 290:
        scoreboard.level_up()
        player.back_at_same_position()
        screen.onkey(key = "Up", fun = player.move_forward)
        car.car_steps += 5

    #detect collision with cars
    for cars in car.all_cars:
        if cars.distance(player) < 20 :
            scoreboard.game_over()
            game = False




screen.exitonclick()