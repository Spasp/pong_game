from turtle import Turtle, Screen
import time
from bat import Bat
from ball import Ball
from scoreboard import Score
import random
screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = True
bat1 = Bat(0)
bat2 = Bat(1)
ball = Ball()
score_right = Score("right")
score_left = Score("left")
screen.listen()
screen.onkeypress(bat1.up, "w")
screen.onkeypress(bat1.down, "s")
screen.onkeypress(bat2.up, "Up")
screen.onkeypress(bat2.down, "Down")
rally = 0
goal_right = 0
goal_left = 0
while game_is_on:
    goal = False

    screen.update()
    time.sleep(0.02)
    ball.move()

    # Goal detection
    if ball.xcor() > 580:
        ball.reset("right")
        bat1.reset()
        bat2.reset()
        score_left.increase_score()
        goal = True
        goal_left += 1
        rally = 0
        ball.decrease_speed()
        if goal_left > 9 :
            score_right.game_over()
            game_is_on = False


    if ball.xcor() < -580:
        ball.reset("left")
        bat1.reset()
        bat2.reset()
        score_right.increase_score()
        goal = True
        goal_right += 1
        rally = 0
        ball.decrease_speed()
        if goal_right > 9:
            score_right.game_over()
            game_is_on = False

    # Detect collision with bats

    if ball.distance(bat2) < 25 or ball.distance(bat2.xcor(),bat2.ycor()+27) < 25 or ball.distance(bat2.xcor(),bat2.ycor()-27)<25 :
        ball.setheading(random.randint(125, 200))
        rally= check_for_rally(rally)



    if ball.distance(bat1) < 25 or ball.distance(bat1.xcor(),bat1.ycor()+27) < 25 or ball.distance(bat1.xcor(),bat1.ycor()-27) < 25:
        ball.setheading(random.randint(-60, 60 ))
        rally = check_for_rally(rally)






    # Detect collision with floor
    if ball.ycor() < -360:
       # ball.setheading(random.randint(3, 60))
        ball.setheading(-ball.heading() )
    # Detect collision with ceiling
    if ball.ycor() > 360:
        ball.setheading(-ball.heading() )
        #ball.setheading(random.randint(-60, -3))



    def check_for_rally(rally):
        if goal == False:
            rally += 1
            if rally == 10:
                rally = 0

                ball.increase_speed()
            return rally






screen.exitonclick()