from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__ (self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 1;
        self.update_scoreborad()
        

    def update_scoreborad(self):
        self.clear()
        self.goto(x = -270, y = 270)
        self.pendown()
        self.write(f"Level : {self.level}", align = "left", font = FONT)
    
    def add_level(self):
        self.level+=1
        self.update_scoreborad();

    def game_over(self):
        self.home()
        self.write("Game Over", align = "Center", font = FONT)
