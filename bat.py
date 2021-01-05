from turtle import Turtle


MOVE_DISTANCE = 25
UP = 90
DOWN = 270
POSITIONS_LEFT = (-545, 0)
POSITION_RIGHT = (545, 0)
SIDE = [POSITIONS_LEFT, POSITION_RIGHT]


class Bat(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.create_bat()

    def create_bat(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(SIDE[self.side])

    def up(self):
        if self.ycor() < 340:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):

        if self.ycor() > -340:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

    def reset(self):
        self.goto(self.xcor(),0)