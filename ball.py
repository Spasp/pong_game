from turtle import Turtle
import time
DISTANCE = 5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.extra = 0
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("red")
        self.speed("fastest")
        self.goto(-510,0)
        self.move()

    def move(self):

        self.forward(DISTANCE + self.extra)


    def reset(self,side):
        if side == "left":
            self.goto(510,0)
            self.setheading(180)
            time.sleep(1)

        else:
            self.goto(-510, 0)
            self.setheading(0)
            time.sleep(1)


    def increase_speed(self):
        self.extra += 2

        self.move()

    def decrease_speed(self):
        self.extra = 0


