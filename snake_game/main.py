from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.press_z, "z")
screen.onkey(snake.press_q, "q")
screen.onkey(snake.press_s, "s")
screen.onkey(snake.press_d, "d")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refesh()
        snake.extend()
        scoreboard.increase_score()

    # Collision with walls
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        scoreboard.new_game()
        snake.reset()

    # Collision with tail
    for segment in snake.tail:
        if snake.head.distance(segment) < 10:
            scoreboard.new_game()
            snake.reset()

screen.exitonclick()
