from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car = []
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        for cars in range(0,len(self.car)-1):
            # cars = self.setheading(180)
            # cars = self.forward(self.speed)
            self.car[cars].setheading(180)
            self.car[cars].forward(self.speed)

    def add_speed(self):
        self.speed += MOVE_INCREMENT

    def generate_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_len= 2.0)
        new_car.penup()
        new_car.goto(x = 300, y = random.randint(-250,260))
        new_car.color(COLORS[random.randint(0,5)])
        self.car.append(new_car)