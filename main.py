import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager=CarManager()
score=Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
screen.title("Turtle Road crossing game")
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()


    #Detect collision with the car

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()


    #Check player finished or not

    if player.is_player_finished():
        player.go_start()
        car_manager.level_up()
        score.level_pass()





screen.exitonclick()
