import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
level = Scoreboard()
car = CarManager()

screen.listen()
screen.onkeypress(player.move,"Up")

car_generation_count = 2
car_count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for i in car.car[0:]:
        if player.distance(i) < 20:
            level.game_over()
            game_is_on = False

    if player.ycor() > 280:
        level.add_level()
        player.restart()
        car.add_speed()

    
    car_count +=1

    if car_count == car_generation_count:
        car.generate_car()
        car_count = 0
    car.move()
    
screen.exitonclick()