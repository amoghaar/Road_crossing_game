import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a player object
player = Player()

# Create a car manager object
car_manager = CarManager()

# Create a scoreboard object
score = Scoreboard()

# Listen for keypress events
screen.listen()
screen.onkeypress(fun=player.move, key="Up")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Delay for smooth animation
    screen.update()  # Update the screen

    # Create cars and move them
    car_manager.creating_cars()
    car_manager.move()

    # Check collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            score.game_over()
            game_is_on = False

    # Check if player reached the finish line
    if player.ycor() == 280:
        player.level_up()
        car_manager.level_up_speed()
        score.level_increase()

# Close the game on click
screen.exitonclick()
