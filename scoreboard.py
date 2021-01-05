from turtle import Turtle
FONT = ("Courier", 22, "normal")
ALIGNMENT = "center"


class Score(Turtle):

    def __init__(self,side):
        super().__init__()
        self.score_value = 0
        self.side = side
        self.write_score()

    def increase_score(self):
        self.score_value += 1
        self.clear()
        self.write_score()

    def reset_score(self):
        self.score_value = 0

    def write_score(self):
        self.penup()

        self.color("white")
        if self.side == "left":
            self.goto(-180,365)
        else:
            self.goto(180,365)
        self.write(f"Score:{self.score_value}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.penup()

        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

